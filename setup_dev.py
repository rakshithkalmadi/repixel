#!/usr/bin/env python3
"""
Setup development environment for re-pixel
"""

import subprocess
import sys
import platform
from pathlib import Path


def run_command(cmd, description):
    """Run a command and handle errors."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True)
        print(f"✅ {description} completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed with exit code {e.returncode}")
        return False


def check_python_version():
    """Check if Python version is compatible."""
    version = sys.version_info
    if version.major == 3 and version.minor >= 7:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} is not compatible")
        print("Re-pixel requires Python 3.7 or higher")
        return False


def install_dependencies():
    """Install all dependencies."""
    commands = [
        ("python -m pip install --upgrade pip", "Upgrading pip"),
        ("pip install -e .", "Installing re-pixel in development mode"),
        ("pip install -e \".[dev]\"", "Installing development dependencies"),
    ]
    
    for cmd, desc in commands:
        if not run_command(cmd, desc):
            return False
    
    return True


def setup_pre_commit():
    """Set up pre-commit hooks."""
    if not run_command("pre-commit install", "Setting up pre-commit hooks"):
        print("⚠️  Pre-commit hooks setup failed (optional)")
    return True


def create_sample_config():
    """Create sample configuration files."""
    config_dir = Path(".vscode")
    config_dir.mkdir(exist_ok=True)
    
    # VS Code settings
    settings_file = config_dir / "settings.json"
    if not settings_file.exists():
        settings_content = """{
    "python.defaultInterpreterPath": "./venv/bin/python",
    "python.formatting.provider": "black",
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.linting.mypyEnabled": true,
    "editor.formatOnSave": true,
    "files.exclude": {
        "**/__pycache__": true,
        "**/*.pyc": true,
        ".pytest_cache": true,
        ".mypy_cache": true,
        "build/": true,
        "dist/": true,
        "*.egg-info/": true
    }
}"""
        settings_file.write_text(settings_content)
        print("✅ Created VS Code settings")
    
    # Launch configuration for debugging
    launch_file = config_dir / "launch.json"
    if not launch_file.exists():
        launch_content = """{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        },
        {
            "name": "Python: Test Current File",
            "type": "python",
            "request": "launch",
            "module": "pytest",
            "args": ["${file}", "-v"],
            "console": "integratedTerminal"
        },
        {
            "name": "Re-pixel CLI",
            "type": "python",
            "request": "launch",
            "module": "repixel.cli",
            "args": ["--help"],
            "console": "integratedTerminal"
        }
    ]
}"""
        launch_file.write_text(launch_content)
        print("✅ Created VS Code launch configuration")


def run_initial_tests():
    """Run tests to verify everything is working."""
    print("🧪 Running initial tests to verify setup...")
    return run_command("python -m pytest tests/ -v --tb=short", "Running test suite")


def main():
    """Main setup process."""
    print("🚀 Setting up Re-pixel development environment")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Check if we're in the right directory
    if not Path("pyproject.toml").exists():
        print("❌ Error: pyproject.toml not found. Make sure you're in the project root.")
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        print("❌ Failed to install dependencies")
        sys.exit(1)
    
    # Create configuration files
    create_sample_config()
    
    # Set up pre-commit (optional)
    setup_pre_commit()
    
    # Run initial tests
    if not run_initial_tests():
        print("⚠️  Some tests failed, but setup is complete")
        print("Please check the test output and fix any issues")
    
    print("\n🎉 Development environment setup complete!")
    print("\n📝 Next steps:")
    print("1. Activate your virtual environment if you haven't already")
    print("2. Start coding! The package is installed in development mode")
    print("3. Run tests with: python -m pytest tests/ -v")
    print("4. Check code quality with: flake8 repixel/ && mypy repixel/")
    print("5. Format code with: black repixel/ tests/ examples/")
    
    print(f"\n🔧 System info:")
    print(f"   OS: {platform.system()} {platform.release()}")
    print(f"   Python: {sys.version}")
    print(f"   Platform: {platform.platform()}")


if __name__ == "__main__":
    main()
