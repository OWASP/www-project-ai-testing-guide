# Quick Reference Guide

## Installation

```bash
pip3 install markdown weasyprint
```

## Basic Usage

1. **Edit `config.txt`**:

```
PROJECT_NAME=OWASP AI Testing Guide
VERSION=Version 1.0
TOC_PATH=ToC.md
OUTPUT_FILE=V1.0/OWASP-AI-Testing-Guide-v1.pdf
COVER_IMAGE=Cover.png
HEADER_IMAGE=header-bg.png
```

2. **Place images** in the same directory as the script:
   - `Cover.png` - Your cover page image
   - `header-bg.png` - Your header logo

3. **Run the generator**:

FIRST STEP - Local Cloning
```bash
git clone https://github.com/OWASP/www-project-ai-testing-guide.git
cd www-project-ai-testing-guide
python3 -m venv venv
source venv/bin/activate
pip install markdown weasyprint
```

USAGE:
```bash
python3 PDFGenerator/PDFGenFinal.py --config PDFGenerator/config.txt
```


```
www-project-ai-testing-guide/
├── PDFGenerator/
│   ├── PDFGenFinal.py      # The generator script
│   ├── config.txt          # Generator configuration
│   ├── ToC.md              # Table of Contents
│   ├── Cover.png           # Cover page image
│   └── header-bg.png       # Header logo
└── Document/
    ├── images/             # Shared images
    │   └── *.png
    └── content/
        └── *.md            # Markdown files
```
