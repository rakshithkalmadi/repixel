import unittest
import tempfile
import shutil
from pathlib import Path
from PIL import Image
import numpy as np

from repixel import ImageCompressor
from repixel.utils import validate_image, get_image_info, calculate_compression_ratio
from repixel.algorithms import JPEGCompressor, PNGCompressor, WebPCompressor


class TestAlgorithmsCustom(unittest.TestCase):
    """Test compression using actual images from input directory, writing to output directory."""
    

    def setUp(self):
        self.input_dir = Path(__file__).parent / "input"
        self.output_dir = Path(__file__).parent / "output"

        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.jpeg_compressor = JPEGCompressor()
        self.png_compressor = PNGCompressor()
        self.webp_compressor = WebPCompressor()

    def tearDown(self):
        """Optional: clear output dir after tests"""
        # Uncomment this if you want to clean output directory after tests
        # shutil.rmtree(self.output_dir)

        pass

    def _compress_and_check(self, compressor, input_path, output_path, **kwargs):
        equivalent_formats = {
            'jpg': 'jpeg',
            'jpeg': 'jpeg',
            'png': 'png',
            'webp': 'webp'
        }
        result = compressor.compress(input_path, output_path, **kwargs)
        self.assertTrue(result.get('success', True), f"Failed to compress {input_path}")
        self.assertTrue(output_path.exists(), f"Output not created: {output_path}")
        self.assertEqual(
            equivalent_formats[result['format'].lower()],
            equivalent_formats[output_path.suffix[1:].lower()]
        )

    def test_jpeg_images(self):
        """Compress all .jpg or .jpeg files in input_images/"""
        for img_path in self.input_dir.glob("*.jp*g"):
            with self.subTest(file=img_path.name):
                output_path = self.output_dir / f"compressed_{img_path.name}"
                self._compress_and_check(
                    self.jpeg_compressor,
                    img_path,
                    output_path,
                    quality=75,
                    optimize=True,
                    progressive=True
                )

    def test_png_images(self):
        """Compress all .png files in input_images/"""
        for img_path in self.input_dir.glob("*.png"):
            with self.subTest(file=img_path.name):
                output_path = self.output_dir / f"compressed_{img_path.name}"
                self._compress_and_check(
                    self.png_compressor,
                    img_path,
                    output_path,
                    quality=85,
                    compress_level=6
                )

    def test_webp_conversion(self):
        """Convert any image (JPEG/PNG) to WebP in output_images/"""
        for img_path in self.input_dir.glob("*.*"):
            if img_path.suffix.lower() not in [".jpg", ".jpeg", ".png"]:
                continue
            with self.subTest(file=img_path.name):
                output_path = self.output_dir / f"{img_path.stem}.webp"
                self._compress_and_check(
                    self.webp_compressor,
                    img_path,
                    output_path,
                    quality=85,
                    method=4
                )

    def test_lossless_webp_from_png(self):
        """Convert PNGs to lossless WebP"""
        for img_path in self.input_dir.glob("*.png"):
            with self.subTest(file=img_path.name):
                output_path = self.output_dir / f"lossless_{img_path.stem}.webp"
                result = self.webp_compressor.compress(
                    img_path,
                    output_path,
                    quality=100,
                    lossless=True
                )
                self.assertTrue(result.get('success', True))
                self.assertTrue(output_path.exists())
                self.assertTrue(result.get('lossless', False))
                self.assertEqual(result['format'], 'WebP')

if __name__ == '__main__':
    unittest.main()