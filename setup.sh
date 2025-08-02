#!/bin/bash
# Quick setup script for Unix-like systems

echo "🚀 Setting up Re-pixel development environment"

# Check if Python 3.7+ is available
python3 --version || { echo "Python 3.7+ is required"; exit 1; }

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "⚡ Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install package in development mode
echo "📥 Installing re-pixel in development mode..."
pip install -e ".[dev]"

echo "✅ Setup complete!"
echo ""
echo "To activate the environment in the future, run:"
echo "  source venv/bin/activate"
echo ""
echo "To run tests:"
echo "  python -m pytest tests/ -v"
echo ""
echo "To run the demo:"
echo "  python demo.py"
