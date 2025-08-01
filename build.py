#!/usr/bin/env python3
"""
Build script for repixel package
"""

import subprocess
import sys
import shutil
from pathlib import Path


def run_command(cmd, description):
    """Run a command and handle errors."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return result
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"Error: {e.stderr}")
        return None


def clean_build():
    """Clean previous build artifacts."""
    print("🧹 Cleaning build artifacts...")
    
    dirs_to_remove = ['build', 'dist', 'repixel.egg-info']
    for dir_name in dirs_to_remove:
        dir_path = Path(dir_name)
        if dir_path.exists():
            shutil.rmtree(dir_path)
            print(f"   Removed {dir_name}/")
    
    print("✅ Build artifacts cleaned")


def run_tests():
    """Run the test suite."""
    result = run_command("python -m pytest tests/ -v", "Running tests")
    return result is not None


def check_code_quality():
    """Run code quality checks."""
    print("🔍 Running code quality checks...")
    
    # Check with flake8
    result1 = run_command("flake8 repixel/ --max-line-length=88 --extend-ignore=E203,W503", "Linting with flake8")
    
    # Check with mypy
    result2 = run_command("mypy repixel/ --ignore-missing-imports", "Type checking with mypy")
    
    return result1 is not None and result2 is not None


def build_package():
    """Build the package."""
    result = run_command("python -m build", "Building package")
    return result is not None


def upload_to_pypi():
    """Upload to PyPI."""
    print("📦 Uploading to PyPI...")
    print("Note: Make sure you have configured your PyPI credentials")
    print("You can use: twine configure")
    
    # Check if user wants to upload to test PyPI first
    response = input("Upload to test PyPI first? (y/n): ").lower().strip()
    
    if response == 'y':
        result = run_command("twine upload --repository testpypi dist/*", "Uploading to test PyPI")
        if result:
            print("✅ Package uploaded to test PyPI!")
            print("You can install it with: pip install --index-url https://test.pypi.org/simple/ repixel")
            
            response = input("Upload to production PyPI? (y/n): ").lower().strip()
            if response == 'y':
                result = run_command("twine upload dist/*", "Uploading to production PyPI")
                if result:
                    print("✅ Package uploaded to production PyPI!")
                    print("You can now install it with: pip install repixel")
    else:
        result = run_command("twine upload dist/*", "Uploading to production PyPI")
        if result:
            print("✅ Package uploaded to production PyPI!")
            print("You can now install it with: pip install repixel")


def main():
    """Main build process."""
    print("🚀 Starting Repixel package build process")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not Path("pyproject.toml").exists():
        print("❌ Error: pyproject.toml not found. Make sure you're in the project root.")
        sys.exit(1)
    
    # Parse command line arguments
    skip_tests = "--skip-tests" in sys.argv
    skip_quality = "--skip-quality" in sys.argv
    upload = "--upload" in sys.argv
    clean_only = "--clean" in sys.argv
    
    # Clean build artifacts
    clean_build()
    
    if clean_only:
        print("🎉 Clean completed!")
        return
    
    # Run tests unless skipped
    if not skip_tests:
        if not run_tests():
            print("❌ Tests failed. Fix tests before building.")
            sys.exit(1)
    else:
        print("⚠️  Skipping tests")
    
    # Run code quality checks unless skipped
    if not skip_quality:
        if not check_code_quality():
            print("⚠️  Code quality checks failed, but continuing with build...")
    else:
        print("⚠️  Skipping code quality checks")
    
    # Build the package
    if not build_package():
        print("❌ Package build failed")
        sys.exit(1)
    
    print("\n📦 Package built successfully!")
    print("Build artifacts:")
    
    dist_path = Path("dist")
    if dist_path.exists():
        for file in dist_path.iterdir():
            print(f"  - {file.name}")
    
    # Upload if requested
    if upload:
        upload_to_pypi()
    else:
        print("\n💡 To upload to PyPI, run:")
        print("   python build.py --upload")
        print("   Or manually: twine upload dist/*")
    
    print("\n🎉 Build process completed successfully!")


if __name__ == "__main__":
    main()
