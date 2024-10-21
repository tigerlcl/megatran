import os
import json


def create_json():
    """Create JSON files from TXT files in the raw data directory."""
    # Define the path to the raw data directory
    raw_data_dir = 'data/raw/'
    
    # Walk through all directories and files in the raw data directory
    for dirpath, dirnames, filenames in os.walk(raw_data_dir):
        for filename in filenames:
            if filename.endswith('.txt'):
                # Create a corresponding JSON filename
                json_filename = filename.replace('.txt', '.json')
                json_file_path = os.path.join(dirpath, json_filename)
                
                # Create the directory for the JSON file if it doesn't exist
                os.makedirs(os.path.dirname(json_file_path), exist_ok=True)
                # Check if the json file already exists
                if not os.path.exists(json_file_path):
                    # Create an empty JSON file
                    with open(json_file_path, 'w') as json_file:
                        json.dump({}, json_file)  # Write an empty JSON object

if __name__ == "__main__":
    create_json()
