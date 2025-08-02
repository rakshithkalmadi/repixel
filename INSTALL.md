# Installation Guide for Re-pixel

## Quick Installation (End Users)

### From PyPI (When Published)
```bash
pip install re-pixel
```

### Test the Installation
```bash
re-pixel --version
re-pixel formats
```

## Development Installation

### Option 1: Automated Setup (Recommended)

**Windows:**
```cmd
git clone https://github.com/rakshithkalmadi/re-pixel.git
cd re-pixel
setup.bat
```

**Linux/macOS:**
```bash
git clone https://github.com/rakshithkalmadi/re-pixel.git
cd re-pixel
chmod +x setup.sh
./setup.sh
```

### Option 2: Manual Setup

1. **Clone the repository:**
```bash
git clone https://github.com/rakshithkalmadi/re-pixel.git
cd re-pixel
```

2. **Create virtual environment:**
```bash
python -m venv venv
```

3. **Activate virtual environment:**

**Windows:**
```cmd
venv\Scripts\activate
```

**Linux/macOS:**
```bash
source venv/bin/activate
```

4. **Install in development mode:**
```bash
pip install -e ".[dev]"
```

### Option 3: Using the Development Setup Script
```bash
python setup_dev.py
```

## Building the Package

### Build for Distribution
```bash
python -m build
```

### Custom Build Script (Alternative)
```bash
python build_package.py
```

### Build Options
- `python build_package.py --skip-tests` - Skip running tests
- `python build_package.py --skip-quality` - Skip code quality checks
- `python build_package.py --upload` - Upload to PyPI after building
- `python build_package.py --clean` - Clean build artifacts only

## Publishing to PyPI

### Prerequisites
1. **Register accounts:**
   - [PyPI](https://pypi.org/account/register/)
   - [Test PyPI](https://test.pypi.org/account/register/) (optional but recommended)

2. **Configure credentials:**
```bash
pip install twine
twine configure
```

### Upload Process

1. **Build the package:**
```bash
python -m build
```

2. **Upload to Test PyPI first (recommended):**
```bash
twine upload --repository testpypi dist/*
```

3. **Test installation from Test PyPI:**
```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ re-pixel
```

4. **Upload to production PyPI:**
```bash
twine upload dist/*
```

### Automated Upload
```bash
python build_package.py --upload
```

## Verification

### Test the Installation
```bash
# Test CLI
re-pixel --version
re-pixel formats

# Test Python API
python -c "import repixel; print('Re-pixel imported successfully')"

# Run demo
python demo.py

# Run tests
python -m pytest tests/ -v
```

## Troubleshooting

### Common Issues

1. **Import errors:** Make sure all dependencies are installed
```bash
pip install -e ".[dev]"
```

2. **OpenCV issues on Linux:**
```bash
sudo apt-get update
sudo apt-get install libgl1-mesa-glx libglib2.0-0
```

3. **Permission errors during upload:**
   - Check PyPI credentials
   - Ensure you have permission for the package name

4. **Build failures:** Check Python version (3.7+ required)
```bash
python --version
```

### Getting Help

- 📖 [Documentation](README.md)
- 🐛 [Issues](https://github.com/rakshithkalmadi/re-pixel/issues)
- 💬 [Discussions](https://github.com/rakshithkalmadi/re-pixel/discussions)

## Environment Variables

You can set these environment variables for custom behavior:

```bash
# Skip certain checks during build
export RE_PIXEL_SKIP_TESTS=1
export RE_PIXEL_SKIP_QUALITY=1

# Custom PyPI repository
export RE_PIXEL_PYPI_REPO=testpypi
```

## CI/CD

The project includes GitHub Actions workflows for:
- Automated testing on multiple Python versions
- Code quality checks
- Security scanning
- Automatic PyPI publishing on releases

See `.github/workflows/ci.yml` for details.
