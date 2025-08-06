# Development Guide

This guide covers the development workflow, building, testing, and installation processes for the re-pixel project.

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- Git
- Virtual environment (recommended)

### Development Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rakshithkalmadi/re-pixel.git
   cd re-pixel
   ```

2. **Create and activate virtual environment:**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   
   # Linux/Mac
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install development dependencies:**
   ```bash
   pip install -e ".[dev]"
   ```

## 🛠️ Development Workflow

### Setting Up the Environment

After cloning and creating your virtual environment:

```bash
# Activate virtual environment (if not already active)
.\venv\Scripts\Activate.ps1  # Windows
# source venv/bin/activate    # Linux/Mac

# Install in development mode
pip install -e .

# Or install with development dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests
python -m pytest tests/ -v

# Run tests with coverage
python -m pytest tests/ -v --cov=repixel --cov-report=html

# Run specific test file
python -m pytest tests/test_repixel.py -v

# Run tests with short traceback
python -m pytest tests/ -v --tb=short
```

### Code Quality

```bash
# Format code with Black
black repixel/

# Check code style with flake8
flake8 repixel/

# Type checking with mypy
mypy repixel/
```

## 🏗️ Building the Package

### Build Distribution Files

```bash
# Install build dependencies
pip install build twine

# Build the package
python -m build
```

This creates:
- `dist/re_pixel-X.X.X-py3-none-any.whl` (wheel format)
- `dist/re_pixel-X.X.X.tar.gz` (source distribution)

### Verify Build

```bash
# Check the built distributions
twine check dist/*

# List contents of wheel
python -m zipfile -l dist/re_pixel-X.X.X-py3-none-any.whl
```

## 📦 Installation Methods

### Method 1: Install from Local Wheel (Recommended)

```bash
# Install the latest built wheel
pip install dist/re_pixel-1.0.1-py3-none-any.whl

# Force reinstall if already installed
pip install dist/re_pixel-1.0.1-py3-none-any.whl --force-reinstall

# Install with upgrade flag
pip install dist/re_pixel-1.0.1-py3-none-any.whl --upgrade
```

### Method 2: Install from Source Distribution

```bash
# Install from tar.gz
pip install dist/re_pixel-1.0.1.tar.gz
```

### Method 3: Development Installation

```bash
# Install in development mode (editable)
pip install -e .

# Install with development dependencies
pip install -e ".[dev]"
```

### Method 4: Install from Local Directory

```bash
# Install from current directory
pip install .

# Install from specific path
pip install /path/to/re-pixel/
```

## 🧪 Testing Installation

After installation, verify everything works:

```bash
# Test CLI
re-pixel --version
re-pixel --help

# Test Python import
python -c "import repixel; print(f'Version: {repixel.__version__}')"

# Test basic functionality
python -c "from repixel import ImageCompressor; c = ImageCompressor(); print('✅ Package works!')"

# Run demo
python demo.py
```

## 🔄 Version Management

### Updating Version

When releasing a new version, update version in these files:

1. **`pyproject.toml`**:
   ```toml
   version = "X.X.X"
   ```

2. **`repixel/__init__.py`**:
   ```python
   __version__ = "X.X.X"
   ```

3. **`CHANGELOG.md`** (add new release entry):
   ```markdown
   ## [X.X.X] - YYYY-MM-DD
   ### Added/Changed/Fixed
   - Description of changes
   ```

4. **`PROJECT_SUMMARY.md`** (update build artifacts):
   ```markdown
   - `re-pixel-X.X.X-py3-none-any.whl`
   - `re-pixel-X.X.X.tar.gz`
   ```

### Automated Version Check

```bash
# Verify version consistency
python -c "
import tomllib
from repixel import __version__

with open('pyproject.toml', 'rb') as f:
    data = tomllib.load(f)
    
pyproject_version = data['project']['version']
init_version = __version__

print(f'pyproject.toml: {pyproject_version}')
print(f'__init__.py: {init_version}')
print(f'✅ Consistent' if pyproject_version == init_version else '❌ Mismatch')
"
```

## 🚀 Publishing

### To Test PyPI

```bash
# Upload to Test PyPI
twine upload --repository testpypi dist/*

# Install from Test PyPI
pip install --index-url https://test.pypi.org/simple/ re-pixel
```

### To Production PyPI

```bash
# Upload to PyPI
twine upload dist/*

# Install from PyPI
pip install re-pixel
```

## 🔧 Troubleshooting

### Common Issues

1. **Import errors after installation:**
   ```bash
   # Reinstall with force
   pip install dist/re_pixel-X.X.X-py3-none-any.whl --force-reinstall
   ```

2. **Virtual environment issues:**
   ```bash
   # Deactivate and reactivate
   deactivate
   .\venv\Scripts\Activate.ps1
   ```

3. **Dependency conflicts:**
   ```bash
   # Create fresh environment
   deactivate
   rm -rf venv  # or rmdir /s venv on Windows
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   pip install -e ".[dev]"
   ```

4. **Build issues:**
   ```bash
   # Clean previous builds
   rm -rf dist/ build/ *.egg-info/
   python -m build
   ```

### Debugging Installation

```bash
# Check installed packages
pip list | grep re-pixel

# Show package information
pip show re-pixel

# Check installation location
python -c "import repixel; print(repixel.__file__)"

# Verify all modules import
python -c "
from repixel import ImageCompressor
from repixel.algorithms import JPEGCompressor, PNGCompressor, WebPCompressor
from repixel.utils import get_image_info
print('✅ All modules imported successfully')
"
```

## 📋 Development Checklist

Before releasing:

- [ ] All tests pass (`python -m pytest tests/ -v`)
- [ ] Code formatted (`black repixel/`)
- [ ] No linting errors (`flake8 repixel/`)
- [ ] Type checking passes (`mypy repixel/`)
- [ ] Version updated in all files
- [ ] CHANGELOG.md updated
- [ ] Package builds successfully (`python -m build`)
- [ ] Distribution files verified (`twine check dist/*`)
- [ ] Local installation works
- [ ] CLI commands work
- [ ] Demo runs successfully
- [ ] Documentation updated

## 🏃‍♂️ Quick Commands

```bash
# Full development cycle
git pull
.\venv\Scripts\Activate.ps1
pip install -e ".[dev]"
python -m pytest tests/ -v
black repixel/
python -m build
pip install dist/re_pixel-X.X.X-py3-none-any.whl --force-reinstall
re-pixel --version
python demo.py

# Quick test cycle
python -m pytest tests/ -v && echo "✅ Tests passed"

# Quick build and install
python -m build && pip install dist/re_pixel-*-py3-none-any.whl --force-reinstall

# Clean and rebuild
rm -rf dist/ build/ *.egg-info/ && python -m build
```

## 📚 Additional Resources

- [Python Packaging Guide](https://packaging.python.org/)
- [Setuptools Documentation](https://setuptools.pypa.io/)
- [PyPI Publishing Guide](https://packaging.python.org/tutorials/packaging-projects/)
- [Semantic Versioning](https://semver.org/)

---

For more information, see the main [README.md](README.md) and [CONTRIBUTING.md](CONTRIBUTING.md) files.
