# Quick Reference Guide

## Installation

```bash
pip3 install markdown weasyprint requests
```

## Basic Usage

1. **Edit `config.txt`**:

```
PROJECT_NAME=OWASP AI Testing Guide
VERSION=Version 1.0
TOC_PATH=/Doc/projects/www-project-ai-testing-guide/ToC.md
OUTPUT_FILE=OWASP-AI-Testing-Guide.pdf
COVER_IMAGE=Cover.png
HEADER_IMAGE=header-bg.png
```

2. **Place images** in the same directory as the script:
   - `Cover.png` - Your cover page image
   - `header-bg.png` - Your header logo

3. **Run the generator**:

FIRST STEP - Local Cloning
```
cd /PDFproject
git clone https://github.com/OWASP/www-project-ai-testing-guide.git
source venv/bin/activate
```

USAGE:
```bash
python3 PDFGenFinal.py --config config.txt
```


```
your-project/
├── PDFGenFinal.py          # The generator script
├── config.txt              # Your configuration
├── Cover.png               # Cover page image
├── header-bg.png           # Header logo
└── www-project-ai-testing-guide/
    ├── ToC.md              # Table of Contents
    ├── Document/
    │   └── images/         # Shared images
    │       └── *.png
    └── content/
        └── *.md            # Markdown files
```



