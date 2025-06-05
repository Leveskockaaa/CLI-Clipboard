import os
import json
import pyperclip
import sys

DATA_FILE = 'data.json'

script_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_dir, DATA_FILE)

def load_data():
    """Load data from the JSON file."""
    try:
        with open(data_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(data):
    """Save data to the JSON file."""
    with open(data_path, 'w') as file:
        json.dump(data, file, indent=4)

def add_entry(key, value):
    """Add a new entry to the clipboard data."""
    data = load_data()
    if key in data:
        print(f"Key '{key}' already exists. Use 'update' to modify it.")
    else:
        data[key] = value
        save_data(data)
        print(f"Added entry: {key} -> {value}")

def update_entry(key, value):
    """Update an existing entry in the clipboard data."""
    data = load_data()
    if key in data:
        data[key] = value
        save_data(data)
        print(f"Updated entry: {key} -> {value}")
    else:
        print(f"Key '{key}' does not exist. Use 'add' to create it.")

def get_entry(key):
    """Retrieve an entry from the clipboard data."""
    data = load_data()
    if key in data:
        pyperclip.copy(data[key])
        print(f"Copied to clipboard: {data[key]}")
    else:
        print(f"Key '{key}' does not exist.")

def delete_entry(key):
    """Delete an entry from the clipboard data."""
    data = load_data()
    if key in data:
        del data[key]
        save_data(data)
        print(f"Deleted entry: {key}")
    else:
        print(f"Key '{key}' does not exist.")

def main():
    """Main function to handle command line arguments."""
    if len(sys.argv) < 3:
        print("Usage: python clipboard.py <command> <key> [value]")
        print("Commands: add, update, get, delete")
        return

    command = sys.argv[1]
    key = sys.argv[2]

    if command == 'add' and len(sys.argv) == 4:
        value = sys.argv[3]
        add_entry(key, value)
    elif command == 'update' and len(sys.argv) == 4:
        value = sys.argv[3]
        update_entry(key, value)
    elif command == 'get':
        get_entry(key)
    elif command == 'delete':
        delete_entry(key)
    else:
        print("Invalid command or arguments.")

if __name__ == "__main__":
    main()