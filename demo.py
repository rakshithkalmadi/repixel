#!/usr/bin/env python3
"""
Re-pixel Demo Script - Create sample images and demonstrate compression
"""

import os
import tempfile
import shutil
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import numpy as np

from repixel import ImageCompressor
from repixel.utils import get_image_info, format_file_size


def create_sample_images(output_dir: Path):
    """Create sample images for demonstration."""
    print("🎨 Creating sample images...")
    
    output_dir.mkdir(exist_ok=True)
    
    # Create a colorful gradient image
    gradient_img = Image.new('RGB', (1920, 1080), color='white')
    draw = ImageDraw.Draw(gradient_img)
    
    # Create gradient effect
    for y in range(1080):
        color = int(255 * (y / 1080))
        draw.line([(0, y), (1920, y)], fill=(color, 128, 255 - color))
    
    gradient_path = output_dir / "gradient_sample.jpg"
    gradient_img.save(gradient_path, "JPEG", quality=95)
    
    # Create a geometric pattern
    pattern_img = Image.new('RGB', (800, 600), color='white')
    draw = ImageDraw.Draw(pattern_img)
    
    # Draw geometric shapes
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
    for i in range(6):
        x = (i % 3) * 250 + 50
        y = (i // 3) * 250 + 50
        color = colors[i]
        draw.rectangle([x, y, x + 150, y + 150], fill=color)
        draw.ellipse([x + 25, y + 25, x + 125, y + 125], fill='white')
    
    pattern_path = output_dir / "pattern_sample.png"
    pattern_img.save(pattern_path, "PNG")
    
    # Create a noisy photo-like image
    photo_array = np.random.randint(0, 255, (600, 800, 3), dtype=np.uint8)
    # Add some structure to make it more photo-like
    for i in range(3):
        photo_array[:, :, i] = np.convolve(photo_array[:, :, i].flatten(), 
                                          np.ones(10)/10, mode='same').reshape(600, 800)
    
    photo_img = Image.fromarray(photo_array.astype(np.uint8))
    photo_path = output_dir / "photo_sample.jpg"
    photo_img.save(photo_path, "JPEG", quality=90)
    
    print(f"✅ Created {len(list(output_dir.glob('*')))} sample images in {output_dir}")
    return [gradient_path, pattern_path, photo_path]


def demonstrate_compression(sample_images: list):
    """Demonstrate various compression techniques."""
    print("\n🗜️  Demonstrating compression techniques...")
    
    compressor = ImageCompressor()
    
    for img_path in sample_images:
        print(f"\n📷 Processing: {img_path.name}")
        
        # Get original info
        original_info = get_image_info(img_path)
        print(f"   Original: {original_info['dimensions']} - {format_file_size(original_info['size_bytes'])}")
        
        # Test different quality settings
        qualities = [95, 85, 70, 50]
        
        for quality in qualities:
            output_path = img_path.parent / f"{img_path.stem}_q{quality}.jpg"
            
            try:
                result = compressor.compress(
                    input_path=img_path,
                    output_path=output_path,
                    quality=quality,
                    format="jpeg"
                )
                
                print(f"   Quality {quality:2d}: {result['compressed_size_mb']:.2f} MB "
                      f"({result['space_saved_percent']:.1f}% reduction)")
                
            except Exception as e:
                print(f"   Quality {quality:2d}: Failed - {e}")


def demonstrate_format_conversion(sample_images: list):
    """Demonstrate format conversion."""
    print("\n🔄 Demonstrating format conversion...")
    
    compressor = ImageCompressor()
    
    # Take the first image and convert to different formats
    source_img = sample_images[0]
    formats = ['jpeg', 'png', 'webp']
    
    print(f"📷 Converting: {source_img.name}")
    
    original_info = get_image_info(source_img)
    print(f"   Original: {format_file_size(original_info['size_bytes'])} ({original_info['format']})")
    
    for fmt in formats:
        output_path = source_img.parent / f"converted.{fmt}"
        
        try:
            result = compressor.compress(
                input_path=source_img,
                output_path=output_path,
                quality=85,
                format=fmt
            )
            
            print(f"   {fmt.upper():4s}: {result['compressed_size_mb']:.2f} MB "
                  f"({result['compression_ratio']:.1%} of original)")
            
        except Exception as e:
            print(f"   {fmt.upper():4s}: Failed - {e}")


def demonstrate_batch_processing(sample_dir: Path):
    """Demonstrate batch processing."""
    print("\n📦 Demonstrating batch processing...")
    
    compressor = ImageCompressor()
    
    output_dir = sample_dir / "batch_compressed"
    
    try:
        results = compressor.compress_batch(
            input_dir=sample_dir,
            output_dir=output_dir,
            quality=80,
            format="webp"
        )
        
        successful = [r for r in results if r.get('success', True)]
        total_original = sum(r.get('original_size_mb', 0) for r in successful)
        total_compressed = sum(r.get('compressed_size_mb', 0) for r in successful)
        
        print(f"   Processed: {len(successful)} images")
        print(f"   Original total: {total_original:.2f} MB")
        print(f"   Compressed total: {total_compressed:.2f} MB")
        print(f"   Total savings: {total_original - total_compressed:.2f} MB "
              f"({((total_original - total_compressed) / total_original * 100):.1f}%)")
        
    except Exception as e:
        print(f"   Batch processing failed: {e}")


def demonstrate_quality_optimization(sample_images: list):
    """Demonstrate quality optimization for target size."""
    print("\n🎯 Demonstrating quality optimization...")
    
    compressor = ImageCompressor()
    
    # Use the largest image
    source_img = sample_images[0]  # Usually the gradient image
    original_info = get_image_info(source_img)
    
    print(f"📷 Optimizing: {source_img.name}")
    print(f"   Original size: {original_info['size_mb']:.2f} MB")
    
    # Try to compress to half the size
    target_size = original_info['size_mb'] * 0.5
    
    try:
        result = compressor.optimize_quality(
            input_path=source_img,
            target_size_mb=target_size,
            format="jpeg"
        )
        
        print(f"   Target size: {target_size:.2f} MB")
        print(f"   Optimal quality: {result['quality']}")
        print(f"   Achieved size: {result['compressed_size_mb']:.2f} MB")
        print(f"   Compression ratio: {result['compression_ratio']:.1%}")
        
    except Exception as e:
        print(f"   Optimization failed: {e}")


def main():
    """Run the complete demonstration."""
    print("🚀 Re-pixel Compression Demo")
    print("=" * 50)
    
    # Create temporary directory for demo
    with tempfile.TemporaryDirectory() as temp_dir:
        demo_dir = Path(temp_dir) / "re_pixel_demo"
        demo_dir.mkdir()
        
        try:
            # Create sample images
            sample_images = create_sample_images(demo_dir)
            
            # Run demonstrations
            demonstrate_compression(sample_images)
            demonstrate_format_conversion(sample_images)
            demonstrate_batch_processing(demo_dir)
            demonstrate_quality_optimization(sample_images)
            
            print("\n🎉 Demo completed successfully!")
            print("\n📝 Try these commands yourself:")
            print("   re-pixel compress image.jpg -q 80 -f webp")
            print("   re-pixel batch photos/ -o compressed/ -q 85")
            print("   re-pixel optimize large.jpg --target-size 2.0")
            print("   re-pixel info image.jpg")
            
        except Exception as e:
            print(f"❌ Demo failed: {e}")
            raise


if __name__ == "__main__":
    main()
