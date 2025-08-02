# Repixel 🎨

[![PyPI version](https://badge.fury.io/py/repixel.svg)](https://badge.fury.io/py/repixel)
[![Python versions](https://img.shields.io/pypi/pyversions/repixel.svg)](https://pypi.org/project/repixel/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Repixel** is a powerful and versatile Python library for image compression that supports multiple formats and algorithms. It provides both a simple Python API and a feature-rich command-line interface for compressing images while maintaining optimal quality.

## ✨ Features

- **Multiple Format Support**: JPEG, PNG, WebP, BMP, TIFF
- **Smart Compression**: Automatic quality optimization for target file sizes
- **Batch Processing**: Compress entire directories with progress tracking
- **Advanced Algorithms**: Multiple compression techniques including lossless options
- **CLI Interface**: Easy-to-use command-line tool with rich output
- **Flexible API**: Simple Python API for integration into your projects
- **Image Analysis**: Detailed image information and compression statistics
- **Resize & Compress**: Automatic resizing with aspect ratio preservation

## 🚀 Installation

### From PyPI (Recommended)

```bash
pip install repixel
```

### From Source

```bash
git clone https://github.com/rakshithkalmadi/repixel.git
cd repixel
pip install -e .
```

### Development Installation

```bash
git clone https://github.com/rakshithkalmadi/repixel.git
cd repixel
pip install -e ".[dev]"
```

## 📖 Quick Start

### Python API

```python
from repixel import ImageCompressor

# Initialize compressor
compressor = ImageCompressor()

# Compress a single image
result = compressor.compress(
    input_path="photo.jpg",
    output_path="photo_compressed.jpg",
    quality=80,
    format="jpeg"
)

print(f"Original size: {result['original_size_mb']:.2f} MB")
print(f"Compressed size: {result['compressed_size_mb']:.2f} MB")
print(f"Space saved: {result['space_saved_percent']:.1f}%")

# Batch compress all images in a directory
results = compressor.compress_batch(
    input_dir="photos/",
    output_dir="compressed_photos/",
    quality=85,
    format="webp",
    recursive=True
)

# Optimize quality for target file size
result = compressor.optimize_quality(
    input_path="large_photo.jpg",
    target_size_mb=2.0,
    format="jpeg"
)
```

### Command-Line Interface

```bash
# Compress a single image
repixel compress photo.jpg -q 80 -f webp -o photo_compressed.webp

# Batch compress images in a directory
repixel batch photos/ -o compressed/ -q 85 -f webp --recursive

# Find optimal quality for target size
repixel optimize large_photo.jpg --target-size 2.0 -f jpeg -o optimized.jpg

# Get image information
repixel info photo.jpg

# List supported formats
repixel formats
```

## 🔧 Advanced Usage

### Custom Compression Settings

```python
from repixel import ImageCompressor

compressor = ImageCompressor()

# JPEG with progressive encoding and sharpening
result = compressor.compress(
    input_path="photo.jpg",
    output_path="optimized.jpg",
    quality=90,
    format="jpeg",
    optimize=True,
    progressive=True,
    enhance_sharpness=True,
    sharpness_factor=1.2
)

# WebP lossless compression
result = compressor.compress(
    input_path="graphic.png",
    output_path="graphic.webp",
    format="webp",
    lossless=True
)

# PNG with color reduction
result = compressor.compress(
    input_path="image.png",
    output_path="compressed.png",
    quality=70,  # Affects color palette reduction
    compress_level=9
)
```

### Resize and Compress

```python
from repixel.algorithms import AdvancedCompressor

# Resize to fit within bounds and compress
result = AdvancedCompressor.resize_and_compress(
    input_path="high_res.jpg",
    output_path="web_optimized.jpg",
    max_width=1920,
    max_height=1080,
    quality=85,
    format="jpeg"
)
```

### Image Information

```python
from repixel.utils import get_image_info, format_file_size

info = get_image_info("photo.jpg")
print(f"Dimensions: {info['dimensions']}")
print(f"File size: {format_file_size(info['size_bytes'])}")
print(f"Format: {info['format']}")
print(f"Megapixels: {info['megapixels']} MP")
```

## 🎛️ CLI Reference

### Commands

- `compress` - Compress a single image
- `batch` - Compress multiple images in a directory
- `optimize` - Find optimal quality for target file size
- `info` - Display image information
- `formats` - List supported formats

### Common Options

- `-q, --quality` - Compression quality (1-100)
- `-f, --format` - Output format (jpeg, png, webp)
- `-o, --output` - Output path
- `--optimize` - Enable optimization
- `--progressive` - Enable progressive JPEG
- `--lossless` - Use lossless compression (WebP)
- `-v, --verbose` - Verbose output

### Examples

```bash
# High quality JPEG compression
repixel compress input.jpg -q 95 -f jpeg --progressive --optimize

# Batch convert to WebP with custom quality
repixel batch photos/ -o webp_photos/ -f webp -q 80 --recursive

# Optimize for web (target 500KB)
repixel optimize large.jpg --target-size 0.5 -f jpeg -o web_ready.jpg

# Get detailed image information
repixel info photo.jpg --verbose
```

## 📊 Format Comparison

| Format | Best For | Compression | Transparency | Animation |
|--------|----------|-------------|--------------|-----------|
| JPEG | Photos, complex images | Lossy, high | ❌ | ❌ |
| PNG | Graphics, simple images | Lossless | ✅ | ❌ |
| WebP | Web images, modern browsers | Both | ✅ | ✅ |

## 🎯 Quality Guidelines

- **95-100**: Maximum quality, minimal compression
- **85-95**: High quality, good for professional use
- **75-85**: Good quality, recommended for web
- **65-75**: Medium quality, smaller file sizes
- **50-65**: Lower quality, significant compression
- **Below 50**: Poor quality, maximum compression

## 🛠️ Development

### Setup Development Environment

```bash
git clone https://github.com/rakshithkalmadi/repixel.git
cd repixel
pip install -e ".[dev]"
```

### Run Tests

```bash
python -m pytest tests/ -v
```

### Code Formatting

```bash
black repixel/
flake8 repixel/
```

### Type Checking

```bash
mypy repixel/
```

## 📦 Building and Publishing

### Build the Package

```bash
python -m build
```

### Upload to PyPI

```bash
twine upload dist/*
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Pillow](https://pillow.readthedocs.io/) for image processing capabilities
- [OpenCV](https://opencv.org/) for advanced image algorithms
- [Click](https://click.palletsprojects.com/) for the CLI interface

## 📞 Support

If you encounter any issues or have questions:

- 🐛 [Report bugs](https://github.com/rakshithkalmadi/repixel/issues)
- 💡 [Request features](https://github.com/rakshithkalmadi/repixel/issues)
- 📧 Contact: your.email@example.com

---

Made with ❤️ by [Rakshith Kalmadi](https://github.com/rakshithkalmadi)

