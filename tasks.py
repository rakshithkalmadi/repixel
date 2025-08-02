"""
Task definitions for project automation using invoke.
Install with: pip install invoke
Run with: invoke [task-name]
"""

import os
import shutil
from invoke import task
from cfg_reader import read_pypirc
import fnmatch
@task
def clean(c):
    """Remove build artifacts."""
    # Directories to remove
    dir_patterns = ["build", "dist", "*.egg-info", "__pycache__", ".pytest_cache"]
    # Files to remove
    file_patterns = ["*.pyc", ".coverage"]
    # Virtual environment directories to exclude
    venv_patterns = ["venv", "env", ".venv", ".env", "virtualenv", "ENV", "env.bak", "venv.bak"]
    
    for root, dirs, files in os.walk(os.getcwd(), topdown=False):
        # Skip if we're inside a virtual environment directory
        rel_root = os.path.relpath(root, os.getcwd())
        if any(venv_dir in rel_root.split(os.sep) for venv_dir in venv_patterns):
            continue
            
        # Check directories
        for dir in dirs:
            # Skip virtual environment directories
            if dir in venv_patterns:
                continue
                
            dir_path = os.path.join(root, dir)
            if any(fnmatch.fnmatch(dir, pattern) for pattern in dir_patterns):
                if os.path.exists(dir_path):
                    print(f"Removing directory: {dir_path}")
                    shutil.rmtree(dir_path, ignore_errors=True)
        
        # Check files
        for file in files:
            file_path = os.path.join(root, file)
            if any(fnmatch.fnmatch(file, pattern) for pattern in file_patterns):
                if os.path.exists(file_path):
                    print(f"Removing file: {file_path}")
                    os.remove(file_path)

@task
def test(c):
    """Run tests."""
    c.run("python -m pytest tests/ -v")

@task
def lint(c):
    """Run linting."""
    c.run("flake8 repixel tests")
    c.run("black --check repixel tests")

@task
def format(c):
    """Format code with Black."""
    c.run("black repixel tests")

@task
def build(c):
    """Build the package."""
    clean(c)
    c.run("python -m build")

@task
def publishtest(c):
    """Publish to TestPyPI."""
    build(c)
    # Try using twine with .pypirc configuration first
    try:
        c.run("twine upload --repository testpypi dist/* --verbose")
    except Exception as e:
        print(f"Failed with .pypirc config: {e}")
        # Fallback to manual authentication
        pypirc_data = read_pypirc()
        if pypirc_data:
            username = pypirc_data.get("testpypi").get("username")
            password = pypirc_data.get("testpypi").get("password")
            c.run(f"twine upload --repository-url https://test.pypi.org/legacy/ dist/* -u {username} -p {password} --verbose")
        else:
            print("No .pypirc file found and initial upload failed.")

@task
def publish(c):
    """Publish to PyPI."""
    build(c)
    # Try using twine with .pypirc configuration first
    try:
        c.run("twine upload dist/* --verbose")
    except Exception as e:
        print(f"Failed with .pypirc config: {e}")
        # Fallback to manual authentication
        pypirc_data = read_pypirc()
        if pypirc_data:
            username = pypirc_data.get("pypi").get("username")
            password = pypirc_data.get("pypi").get("password")
            c.run(f"twine upload dist/* -u {username} -p {password} --verbose")
        else:
            print("No .pypirc file found and initial upload failed.")
