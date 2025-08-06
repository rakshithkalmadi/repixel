# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.1] - 2025-08-06

### Changed
- Improved PNG compression efficiency by preserving palette mode
- Increased default PNG compression level to 9 (maximum compression)
- Enhanced WebP compression with better optimization settings
- Removed image enhancement features to focus purely on compression
- Streamlined OpenCV compressor for better performance

### Fixed
- PNG palette compression now properly maintains palette mode instead of converting back to RGB
- Improved compression ratios across all supported formats

## [1.0.0] - 2025-08-01

### Added
- Initial release of Re-pixel image compression library
- Multi-format support (JPEG, PNG, WebP, BMP, TIFF)
- Smart compression with quality optimization
- Batch processing capabilities
- Command-line interface with rich features
- Advanced compression algorithms
- Image resize and compress functionality
- Comprehensive test suite
- Documentation and examples

### Features
- Single image compression with customizable quality
- Batch directory processing with recursive support
- Automatic quality optimization for target file sizes
- Progressive JPEG and lossless WebP support
- Image information extraction and analysis
- Multiple compression methods and algorithms
- CLI with progress bars and detailed output
- Cross-platform support (Windows, macOS, Linux)

### API
- `ImageCompressor` main class
- `JPEGCompressor`, `PNGCompressor`, `WebPCompressor` algorithms
- `AdvancedCompressor` for special techniques
- Utility functions for image validation and information
- Complete type hints and documentation
