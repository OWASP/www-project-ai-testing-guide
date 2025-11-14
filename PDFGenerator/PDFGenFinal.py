
#!/usr/bin/env python3
import argparse
import re
import subprocess
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from markdown import markdown
from weasyprint import HTML

VALIDATE_STRUCTURE = False


# ------------------ Configuration Management ------------------ #

def load_config(config_path: Path) -> dict:
    """Load configuration from a text file."""
    config = {
        'PROJECT_NAME': 'Document',
        'VERSION': 'Version 1.0',
        'TOC_PATH': 'ToC.md',
        'OUTPUT_FILE': 'output.pdf',
        'COVER_IMAGE': '',
        'HEADER_IMAGE': ''
    }
    
    if not config_path.exists():
        print(f"⚠ Config file not found: {config_path}")
        return config
    
    print(f"Loading configuration from: {config_path}")
    
    with open(config_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # Skip comments and empty lines
            if not line or line.startswith('#'):
                continue
            
            # Parse KEY=VALUE
            if '=' in line:
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()
                
                if key in config:
                    config[key] = value
                    print(f"  {key} = {value}")
    
    return config


# ------------------ Utility functions ------------------ #

def sanitize_heading(text: str) -> str:
    """Create a safe HTML id from heading text."""
    return re.sub(r'[^a-zA-Z0-9_-]', '', text.replace(' ', '_'))


def get_git_info():
    """Return (branch, short_commit) or ('unknown', 'unknown')."""
    try:
        commit = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"]
        ).decode().strip()
        branch = subprocess.check_output(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"]
        ).decode().strip()
        return branch, commit
    except Exception:
        return "unknown", "unknown"


def transform_special_blockquotes(md_text: str) -> str:
    """Convert custom NOTE/COMMENT blockquotes in markdown to styled HTML blockquotes."""
    md_text = re.sub(
        r'(?m)^> NOTE:\s*(.*)',
        r'<blockquote class="note"><strong>Note:</strong> \1</blockquote>',
        md_text
    )
    md_text = re.sub(
        r'(?m)^> COMMENT:\s*(.*)',
        r'<blockquote class="comment"><strong>Comment:</strong> \1</blockquote>',
        md_text
    )
    return md_text


def validate_markdown(file_path: Path, html: str):
    """Optionally ensure markdown has at least one h1, etc."""
    headings = re.findall(r'<h([123])>(.*?)</h\1>', html)

    if VALIDATE_STRUCTURE:
        if not any(level == '1' for level, _ in headings):
            raise ValueError(f"Validation failed: No <h1> heading found in {file_path}")

    return headings


def resolve_image_paths(html: str, base_path: Path, repo_root: Path = None) -> str:
    """
    Convert <img src="relative"> to absolute file:// paths for WeasyPrint (local files).
    Improved version with better error handling and path resolution.
    Handles /Document/images/ paths relative to repository root.
    """
    def repl(match):
        # Extract the full img tag and src attribute
        full_tag = match.group(0)
        src = match.group(1)
        
        # Skip if already absolute URL or file://
        if src.startswith(('http://', 'https://', 'file://', 'data:')):
            return full_tag
        
        # Try multiple resolution strategies
        possible_paths = []
        
        # Strategy 1: If path starts with /Document/, resolve from repo root
        if src.startswith('/Document/') and repo_root:
            # Remove leading slash and resolve from repo root
            rel_path = src.lstrip('/')
            possible_paths.append(repo_root / rel_path)
        
        # Strategy 2: Relative to markdown file
        possible_paths.append(base_path / src)
        
        # Strategy 3: One level up from markdown file
        possible_paths.append(base_path.parent / src)
        
        # Strategy 4: Two levels up (for nested content)
        possible_paths.append(base_path.parent.parent / src)
        
        # Strategy 5: Absolute path as-is
        if not src.startswith('/'):
            possible_paths.append(Path(src))
        
        # Strategy 6: Remove leading slashes or dots
        cleaned_src = src.lstrip('./')
        possible_paths.append(base_path / cleaned_src)
        
        # Strategy 7: If starts with /, try from repo root
        if src.startswith('/') and repo_root:
            possible_paths.append(repo_root / src.lstrip('/'))
        
        # Find first existing path
        abs_path = None
        for path in possible_paths:
            try:
                resolved = path.resolve()
                if resolved.exists():
                    abs_path = resolved
                    break
            except (OSError, ValueError):
                continue
        
        if abs_path is None:
            print(f"⚠ Warning: Image file not found: {src}")
            print(f"   Searched from: {base_path}")
            if repo_root:
                print(f"   Repository root: {repo_root}")
            print(f"   Tried {len(possible_paths)} possible paths")
            # Return original tag but with a placeholder style
            return f'<div class="missing-image">⚠ Missing image: {src}</div>'
        else:
            print(f"✓ Embedding image: {src} → {abs_path}")
            # Return img tag with file:// URL and proper styling
            return f'<img src="file://{abs_path}" style="display:block;margin:2em auto;max-width:100%;height:auto;" />'

    return re.sub(r'<img\s+[^>]*src="([^"]+)"[^>]*>', repl, html)


def parse_toc_file(toc_path: Path):
    print(f"\nParsing ToC file: {toc_path}")
    toc_content = toc_path.read_text(encoding="utf-8")

    link_pattern = r'\[([^\]]+)\]\(([^)]+\.md)\)'
    matches = re.findall(link_pattern, toc_content)

    file_refs = []
    toc_dir = toc_path.parent
    
    # repo locale clonato accanto allo script
    REPO_ROOT = (Path(__file__).parent / "www-project-ai-testing-guide").resolve()
    GITHUB_PREFIX = "https://github.com/OWASP/www-project-ai-testing-guide/blob/main/"

    for title, href in matches:
        if href.startswith(GITHUB_PREFIX):
            rel_path = href[len(GITHUB_PREFIX):]
            abs_path = (REPO_ROOT / rel_path).resolve()
        else:
            abs_path = (toc_dir / href).resolve()

        if abs_path.exists():
            print(f"  ✓ Local file: {href} → {abs_path}")
            file_refs.append((href, abs_path))
        else:
            print(f"  ⚠ Missing file: {href} → {abs_path}")

    print(f"Total entries found: {len(file_refs)}")
    return file_refs


def scan_directory(input_dir: Path):
    """Fallback: scan a directory for .md files (not used if you work with ToC.md)."""
    print(f"\nScanning directory: {input_dir}")
    markdown_files = sorted(input_dir.rglob('*.md'), key=lambda p: str(p))
    print(f"Total files found: {len(markdown_files)}")
    return [(str(p), p) for p in markdown_files]


def rewrite_links_to_anchors(html: str, link_map: dict[str, str]) -> str:
    """Replace href="URL" with href="#anchor" when URL is present in link_map."""
    def repl(match):
        href = match.group(1)
        if href in link_map:
            return f'href="#{link_map[href]}"'
        return match.group(0)

    return re.sub(r'href="([^"]+)"', repl, html)


# ------------------ Main PDF generation ------------------ #

def generate_pdf(input_path: Path, output_file: Path, project_name: str = "Document", 
                 version: str = "Version 1.0", cover_image_path: str = "", 
                 header_image_path: str = ""):
    print(">>> PDF Generator - Final Version with Config Support")
    print(f">>> Running from: {__file__}")
    print(f">>> Project: {project_name}")
    print(f">>> Version: {version}")
    
    # Determine repository root
    # Try to find www-project-ai-testing-guide directory
    REPO_ROOT = None
    if input_path.is_file():
        # Start from ToC file's directory and search upwards
        current = input_path.parent.resolve()
    else:
        current = input_path.resolve()
    
    # Search for repository root (contains Document folder)
    while current != current.parent:
        if (current / "Document").exists():
            REPO_ROOT = current
            print(f">>> Repository root detected: {REPO_ROOT}")
            break
        current = current.parent
    
    if REPO_ROOT is None:
        # Fallback: check if script is in repo
        script_parent = Path(__file__).parent / "www-project-ai-testing-guide"
        if script_parent.exists():
            REPO_ROOT = script_parent.resolve()
            print(f">>> Repository root (from script): {REPO_ROOT}")
    
    # 1) Read ToC or scan directory
    toc_html = None

    if input_path.is_file():
        print("Mode: ToC file")
        toc_md = input_path.read_text(encoding="utf-8")
        toc_md = transform_special_blockquotes(toc_md)
        toc_html = markdown(toc_md, extensions=['extra', 'nl2br', 'sane_lists', 'attr_list'])
        file_entries = parse_toc_file(input_path)
    elif input_path.is_dir():
        print("Mode: Directory scan")
        file_entries = scan_directory(input_path)
        toc_html = "<h2>Table of Contents</h2>"
    else:
        raise ValueError(f"Input path does not exist: {input_path}")

    if not file_entries:
        raise ValueError("No markdown files found to process")

    # 2) Build link map: href -> doc anchor id (doc1, doc2, ...)
    link_map: dict[str, str] = {}
    for idx, (href, _) in enumerate(file_entries):
        link_map[href] = f"doc{idx + 1}"

    # rewrite ToC links to internal anchors
    if toc_html is not None:
        toc_html = rewrite_links_to_anchors(toc_html, link_map)

    content_blocks: list[str] = []

    print(f"\nProcessing {len(file_entries)} files...")
    for href, ref in file_entries:
        doc_anchor = link_map[href]
        print(f"\n  Processing [{doc_anchor}]: {ref}")

        # ref è SEMPRE un Path locale
        raw_md = ref.read_text(encoding="utf-8")
        base_path = ref.parent

        # NOTE/COMMENT
        raw_md = transform_special_blockquotes(raw_md)

        # Markdown -> HTML
        html = markdown(raw_md, extensions=['extra', 'nl2br', 'sane_lists', 'attr_list'])

        # Immagini locali -> file:// (improved resolution)
        html = resolve_image_paths(html, base_path, REPO_ROOT)

        # Rewrite links to internal anchors
        html = rewrite_links_to_anchors(html, link_map)

        # Add id to headings
        headings = validate_markdown(ref, html)
        for level, heading in headings:
            anchor = sanitize_heading(heading)
            html = html.replace(
                f"<h{level}>{heading}</h{level}>",
                f"<h{level} id=\"{anchor}\">{heading}</h{level}>"
            )

        # Avvolgi ogni documento in <div id="docX">
        html = f'<div id="{doc_anchor}">{html}</div>'
        content_blocks.append(html)


    # Cover image + header logo
    if cover_image_path:
        cover_path = Path(cover_image_path).resolve()
        if not cover_path.exists():
            # Try relative to script
            cover_path = (Path(__file__).parent / cover_image_path).resolve()
    else:
        cover_path = (Path(__file__).parent / "Cover.png").resolve()
    
    if not cover_path.exists():
        print(f"⚠ Cover image not found at {cover_path}, generating PDF without image cover.")
        cover_img_html = ""
    else:
        cover_src = f"file://{cover_path}"
        cover_img_html = f'<img src="{cover_src}" class="cover-image" />'
        print(f"✓ Cover image found: {cover_path}")

    if header_image_path:
        header_bg_path = Path(header_image_path).resolve()
        if not header_bg_path.exists():
            # Try relative to script
            header_bg_path = (Path(__file__).parent / header_image_path).resolve()
    else:
        header_bg_path = (Path(__file__).parent / "header-bg.png").resolve()
    
    if not header_bg_path.exists():
        print(f"⚠ Header image not found at {header_bg_path}, generating header without logo.")
        header_content = '""'
    else:
        header_bg_url = f"file://{header_bg_path}"
        header_content = f'url("{header_bg_url}")'
        print(f"✓ Header image found: {header_bg_path}")

    # CSS - FINAL VERSION with all fixes
    css = """
@page {{
  size: A4;
  margin: 2.5cm 2.5cm 2cm 2.5cm;

  @top-left {{
    content: "{project_name}";
    font-size: 10pt;
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    color: #103595;
    font-weight: 500;
    vertical-align: bottom;
    padding: 0.7cm 0.0cm;          /* Padding for badge effect */
    border-radius: 0px;            /* Rounded corners */
  }}

  @top-center {{
    content: "";
  }}

  @top-right {{
    content: {header_content};
    vertical-align: bottom;
    padding-bottom: 0.3cm;
  }}

  @bottom-left {{
    content: "{version}";
    font-size: 8pt;
    color: #666;
    vertical-align: top;
    padding-top: 0.2cm;
  }}

  @bottom-right {{
    content: "Page " counter(page) " of " counter(pages);
    font-size: 8pt;
    color: #666;
    vertical-align: top;
    padding-top: 0.2cm;
  }}
}}

@page cover {{
  size: A4;
  margin: 0 0 -0.5cm 0;
  background: none;

  @top-left     {{ content: none; }}
  @top-center   {{ content: none; }}
  @top-right    {{ content: none; }}
  @bottom-left  {{ content: none; }}
  @bottom-center{{ content: none; }}
  @bottom-right {{ content: none; }}
}}

body {{
  font-family: 'Georgia', 'Times New Roman', serif;
  font-size: 11pt;
  line-height: 1.6;
  color: #333;
  margin: 0;
}}

.cover {{
  page: cover;
  width: 100%;
  height: 100vh;
  page-break-after: always;
  display: flex;
  align-items: center;
  justify-content: center;
}}

.cover-image {{
  width: 100%;
  height: 100%;
  object-fit: contain;
  object-position: center center;
  margin: 0;
  padding: 0;
}}

.main {{
  margin: 0 auto;
  max-width: 75ch;
}}

.toc {{
  page-break-after: always;
}}

/* Professional color scheme: Deep Blue for h1, Medium Blue for h2, Dark Gray for h3 */

h1, h2, h3, h4, h5, h6 {{
  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  font-weight: 600;
  line-height: 1.3;
  page-break-after: avoid;
}}

h1 {{
  font-size: 1.8em;           /* Reduced from 2.4em */
  color: #1e3a5f;             /* Deep Blue */
  margin-top: 2em;
  margin-bottom: 0.6em;
  padding-bottom: 0.3em;
  border-bottom: 2px solid #2c5aa0;
  page-break-before: always;
  page-break-after: avoid;
  letter-spacing: -0.02em;
}}

h2 {{
  font-size: 1.4em;           /* Reduced from 1.8em */
  color: #2c5aa0;             /* Medium Blue */
  margin-top: 1.5em;
  margin-bottom: 0.5em;
  page-break-after: avoid;
  letter-spacing: -0.01em;
}}

h3 {{
  font-size: 1.15em;          /* Reduced from 1.4em */
  color: #34495e;             /* Dark Gray */
  margin-top: 1.2em;
  margin-bottom: 0.4em;
  page-break-after: avoid;
  font-weight: 600;
}}

h4 {{
  font-size: 1.05em;
  color: #555;
  margin-top: 1em;
  margin-bottom: 0.3em;
  page-break-after: avoid;
  font-weight: 600;
}}

p {{
  text-align: justify;
  hyphens: auto;
  margin: 0.8em 0;
}}

p, li, table, blockquote {{
  orphans: 2;
  widows: 2;
}}

/* Image styling */
img {{
  display: block;
  margin: 1.5em auto;
  max-width: 100%;
  height: auto;
  border: 1px solid #e0e0e0;
  padding: 0.5em;
  background: #fafafa;
}}

.missing-image {{
  display: block;
  margin: 1.5em auto;
  padding: 1em;
  background: #fff3cd;
  border: 1px solid #ffc107;
  color: #856404;
  text-align: center;
  font-style: italic;
}}

/* Lists */
ul, ol {{
  margin: 0.8em 0;
  padding-left: 2em;
}}

li {{
  margin: 0.3em 0;
}}

/* Code blocks */
code {{
  font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
  font-size: 0.85em;
  background-color: #f5f5f5;
  padding: 0.2em 0.4em;
  border-radius: 3px;
  word-wrap: break-word;
}}

pre {{
  background-color: #f5f5f5;
  border: 1px solid #ddd;
  border-left: 3px solid #2c5aa0;
  padding: 0.8em;
  overflow-x: auto;
  overflow-wrap: break-word;
  word-wrap: break-word;
  white-space: pre-wrap;
  margin: 1em 0;
  page-break-inside: avoid;
  font-size: 0.85em;
  line-height: 1.4;
}}

pre code {{
  background: none;
  padding: 0;
  word-wrap: break-word;
  white-space: pre-wrap;
}}

/* Tables */
table {{
  width: 100%;
  border-collapse: collapse;
  margin: 1.5em 0;
  font-size: 10pt;
  table-layout: auto;
}}

th {{
  background-color: #2c5aa0;
  color: white;
  font-weight: 600;
  border: 1px solid #1e3a5f;
  padding: 8px 10px;
  text-align: left;
  vertical-align: top;
}}

td {{
  border: 1px solid #ddd;
  padding: 6px 10px;
  text-align: left;
  vertical-align: top;
  word-wrap: break-word;
  white-space: normal;
}}

tr:nth-child(even) {{
  background-color: #f9f9f9;
}}

/* Blockquotes */
blockquote {{
  background-color: #f5f5f5;
  border-left: 4px solid #2c5aa0;
  padding: 0.8em 1.2em;
  margin: 1em 0;
  font-size: 0.95em;
  font-style: italic;
}}

blockquote.note {{
  background-color: #fff8dc;
  border-left: 4px solid #f0ad4e;
}}

blockquote.comment {{
  background-color: #e7f3ff;
  border-left: 4px solid #2c5aa0;
}}

/* Links */
a {{
  color: #2c5aa0;
  text-decoration: none;
}}

a:hover {{
  text-decoration: underline;
}}

/* Horizontal rules */
hr {{
  border: none;
  border-top: 1px solid #ddd;
  margin: 2em 0;
}}
""".format(header_content=header_content, project_name=project_name, version=version)

    combined_html = """
<html>
<head>
  <meta charset="utf-8">
  <style>
{css}
  </style>
</head>
<body>
  <div class="cover">
    {cover_img}
  </div>
  <div class="main">
    <div class="toc">
      {toc_html}
    </div>
    {content}
  </div>
</body>
</html>
""".format(
        css=css,
        cover_img=cover_img_html,
        toc_html=toc_html or "",
        content="".join(content_blocks),
    )

    output_file.parent.mkdir(parents=True, exist_ok=True)
    print(f"\n{'='*60}")
    print(f"Generating PDF: {output_file}")
    print(f"{'='*60}")
    
    HTML(string=combined_html, base_url=str(Path(__file__).parent)).write_pdf(str(output_file))
    
    print(f"\n✓ PDF generated successfully!")
    print(f"  Output: {output_file}")
    print(f"  Size: {output_file.stat().st_size / 1024:.1f} KB")


# ------------------ CLI entrypoint ------------------ #

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate PDF from markdown files with optional configuration file support."
    )
    parser.add_argument(
        "--config",
        "-c",
        type=Path,
        help="Path to configuration file (config.txt)",
    )
    parser.add_argument(
        "input_path",
        type=Path,
        nargs='?',
        help="Path to ToC markdown file OR root directory containing markdown files (overrides config)",
    )
    parser.add_argument(
        "output_file",
        type=Path,
        nargs='?',
        help="Path to output PDF file (overrides config)",
    )

    args = parser.parse_args()
    
    # Load configuration if provided
    if args.config:
        config = load_config(args.config)
        
        # Use command line arguments if provided, otherwise use config
        input_path = args.input_path if args.input_path else Path(config['TOC_PATH'])
        output_file = args.output_file if args.output_file else Path(config['OUTPUT_FILE'])
        project_name = config['PROJECT_NAME']
        version = config['VERSION']
        cover_image = config['COVER_IMAGE']
        header_image = config['HEADER_IMAGE']
    else:
        # Traditional mode: require both arguments
        if not args.input_path or not args.output_file:
            parser.error("input_path and output_file are required when not using --config")
        
        input_path = args.input_path
        output_file = args.output_file
        project_name = "Document"
        version = "Version 1.0"
        cover_image = ""
        header_image = ""
    
    generate_pdf(input_path, output_file, project_name, version, cover_image, header_image)