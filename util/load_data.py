import os
import json
    
DATASET_DICT = {
    "TDE-v2": {
        "path": "./data/TDE-v2/benchmark-stackoverflow"
    }
}


def load_dataset_by_name(dataset_name):
    """Load the dataset based on the dataset_name from the configuration."""

    dataset_info = DATASET_DICT.get(dataset_name, None)
    if dataset_info is None:
        raise ValueError(f"Dataset '{dataset_name}' not found in the configuration.")
    
    # Load the dataset using the datasets library
    if dataset_name == "TDE-v2":
        return _load_tde_v2(dataset_info)


def _load_tde_v2(dataset_info: dict):
    # load all json files in the directory
    data = []
    
    for file in os.listdir(dataset_info["path"]):
        if file.endswith('.json'):
            json_fp = os.path.join(dataset_info["path"], file)
            with open(json_fp, 'r') as f:
                obj = json.load(f)
                obj['file_path'] = json_fp
                data.append(obj)

    return data
