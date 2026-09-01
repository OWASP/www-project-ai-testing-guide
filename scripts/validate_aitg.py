#!/usr/bin/env python3
"""
OWASP AI Testing Guide (AITG) Validation Tool

Validates:
1. Test case structure against TestTemplate.md (Summary, Objectives, How to Test, Expected Output, Remediation, Suggested Tools, References).
2. Markdown links for empty targets or malformed URLs.
3. Completeness and consistency of Table of Contents in Document/README.md and PDFGenerator/ToC.md.
"""

import os
import sys
import re
import argparse
from pathlib import Path

# ANSI colors
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
BOLD = "\033[1m"
RESET = "\033[0m"

REQUIRED_SECTIONS = [
    (r"#\s+AITG-[A-Z]+-\d+", "Title header (# AITG-XXX-YY)"),
    (r"###\s+Summary", "### Summary"),
    (r"###\s+Test Objectives", "### Test Objectives"),
    (r"###\s+How to Test", "### How to Test/Payloads"),
    (r"###\s+Expected Output", "### Expected Output"),
    (r"###\s+Remediation", "### Remediation"),
    (r"###\s+Suggested Tools", "### Suggested Tools"),
    (r"###\s+References", "### References"),
]

LINK_REGEX = re.compile(r"\[([^\]]+)\]\(([^)]*)\)")


def get_repo_root() -> Path:
    """Find the root directory of the repository."""
    current = Path(__file__).resolve().parent
    while current != current.parent:
        if (current / ".git").exists() or (current / "Document").exists():
            return current
        current = current.parent
    return Path.cwd()


def validate_test_case(filepath: Path) -> list[str]:
    """Validate a single test case markdown file against required sections and formatting rules."""
    errors = []
    content = filepath.read_text(encoding="utf-8", errors="ignore")
    lines = content.splitlines()

    # 1. Section headers check
    for pattern, name in REQUIRED_SECTIONS:
        if not re.search(pattern, content, re.IGNORECASE):
            errors.append(f"Missing mandatory section: {name}")

    # 2. Empty or malformed markdown links check
    for idx, line in enumerate(lines, 1):
        for match in LINK_REGEX.finditer(line):
            text, url = match.groups()
            clean_url = url.strip()
            if not clean_url:
                errors.append(f"Line {idx}: Empty link target for '[{text}]()'")
            elif " " in clean_url and not clean_url.startswith('"'):
                errors.append(f"Line {idx}: Unescaped whitespace in URL '[{text}]({url})'")

    return errors


def validate_toc_coverage(repo_root: Path) -> list[str]:
    """Ensure all test cases in Document/content/tests are properly indexed."""
    errors = []
    tests_dir = repo_root / "Document" / "content" / "tests"
    readme_file = repo_root / "Document" / "README.md"
    toc_file = repo_root / "PDFGenerator" / "ToC.md"

    if not tests_dir.exists():
        return [f"Directory not found: {tests_dir}"]

    test_files = [
        f.name for f in tests_dir.glob("*.md")
        if f.name != "TestTemplate.md"
    ]

    readme_content = readme_file.read_text(encoding="utf-8", errors="ignore") if readme_file.exists() else ""
    toc_content = toc_file.read_text(encoding="utf-8", errors="ignore") if toc_file.exists() else ""

    for tf in sorted(test_files):
        if tf not in readme_content:
            errors.append(f"Test '{tf}' is missing from Document/README.md")
        if toc_file.exists() and tf not in toc_content:
            errors.append(f"Test '{tf}' is missing from PDFGenerator/ToC.md")

    return errors


def main():
    parser = argparse.ArgumentParser(description="Validate OWASP AI Testing Guide Markdown content and structure.")
    parser.add_argument("--tests-only", action="store_true", help="Only validate test case files")
    parser.add_argument("--toc-only", action="store_true", help="Only validate Table of Contents coverage")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors")
    args = parser.parse_args()

    repo_root = get_repo_root()
    tests_dir = repo_root / "Document" / "content" / "tests"

    print(f"\n{BOLD}{BLUE}==================================================={RESET}")
    print(f"{BOLD}{BLUE}  OWASP AI Testing Guide (AITG) Content Validator  {RESET}")
    print(f"{BOLD}{BLUE}==================================================={RESET}\n")
    print(f"Repository Root: {repo_root}")

    total_errors = 0
    test_files_checked = 0

    if not args.toc_only and tests_dir.exists():
        print(f"\n{BOLD}Validating Test Cases ({tests_dir})...{RESET}")
        test_files = sorted([
            f for f in tests_dir.glob("*.md")
            if f.name != "TestTemplate.md"
        ])

        for tf in test_files:
            test_files_checked += 1
            rel_path = tf.relative_to(repo_root)
            errs = validate_test_case(tf)
            if errs:
                total_errors += len(errs)
                print(f"  {RED}FAIL{RESET} {rel_path}")
                for e in errs:
                    print(f"       - {e}")
            else:
                print(f"  {GREEN}PASS{RESET} {rel_path}")

    if not args.tests_only:
        print(f"\n{BOLD}Validating Table of Contents (ToC) Coverage...{RESET}")
        toc_errors = validate_toc_coverage(repo_root)
        if toc_errors:
            total_errors += len(toc_errors)
            for e in toc_errors:
                print(f"  {RED}FAIL{RESET} {e}")
        else:
            print(f"  {GREEN}PASS{RESET} All test cases are properly indexed in Document/README.md and ToC.md.")

    print(f"\n{BOLD}---------------------------------------------------{RESET}")
    if total_errors == 0:
        print(f"{BOLD}{GREEN}✓ Validation Successful! ({test_files_checked} test files verified, 0 errors){RESET}\n")
        return 0
    else:
        print(f"{BOLD}{RED}✗ Validation Failed: {total_errors} issue(s) detected.{RESET}\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
