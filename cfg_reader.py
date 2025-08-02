import os
from configparser import RawConfigParser

def read_pypirc(filepath=None):
    """
    Reads and parses a .pypirc file.

    Args:
        filepath (str, optional): Path to the .pypirc file. Defaults to None.

    Returns:
        dict: A dictionary representing the parsed .pypirc file, or None if the file doesn't exist.
    """
    if filepath is None:
        # Try home directory first (standard location)
        home_pypirc = os.path.expanduser("~/.pypirc")
        if os.path.exists(home_pypirc):
            filepath = home_pypirc
        else:
            # Fall back to project directory
            filepath = os.path.join(os.path.dirname(__file__), ".pypirc")

    if not os.path.exists(filepath):
        return None
    
    config = RawConfigParser()
    config.read(filepath)
    
    pypirc_data = {}
    for section in config.sections():
        pypirc_data[section] = dict(config.items(section))
    
    return pypirc_data

if __name__ == "__main__":
    pypirc_data = read_pypirc()
    # print(pypirc_data.get("testpypi").get("password"))
    if pypirc_data:
        for section, items in pypirc_data.items():
            print(f"[{section}]")
            for key, value in items.items():
                print(f"  {key} = {value}")
    else:
        print("No .pypirc file found.")