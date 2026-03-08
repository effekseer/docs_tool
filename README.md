# Effekseer Docs Tool

This repository builds the Effekseer HTML documentation with Sphinx.

## Requirements

- Python 3
- pip
- virtualenv
- `make` on macOS or Linux

Install the Python dependencies in a virtual environment. This keeps the docs
toolchain isolated from globally installed Python tools such as Poetry.

## Setup on macOS / Linux

```bash
python3 -m pip install --user --upgrade pip virtualenv
python3 -m virtualenv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
make html
```

## Setup on Windows

```powershell
py -m pip install --user --upgrade pip virtualenv
py -m virtualenv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
make.bat html
```

## Output

The generated HTML files are written to `build/html`.

## Preview and verification

Do not open the generated files with `file://...` in a browser. Some pages embed
effect viewers in `iframe` elements, and those viewers load `.wasm` and effect
files at runtime. Browsers often block those requests when the page is opened
directly from the filesystem.

Use a local HTTP server instead.

### macOS / Linux

```bash
python3 Scripts/preview_docs.py
```

Then open `http://127.0.0.1:8000/`.

To use a different port:

```bash
python3 Scripts/preview_docs.py --port 8080
```

### Windows

```powershell
python Scripts/preview_docs.py
```

Then open `http://127.0.0.1:8000/`.
