import os
import json
    
DATASET_DICT = {
    "stackoverflow": {
        "path": "./data/TDE-v2/benchmark-stackoverflow"
    },
    "bingquery-logs": {
        "path": "./data/TDE-v2/benchmark-bing-query-logs"
    }
}


def load_dataset_by_name(dataset_name):
    """Load the dataset based on the dataset_name from the configuration."""

    dataset_info = DATASET_DICT.get(dataset_name, None)
    if dataset_info is None:
        raise ValueError(f"Dataset '{dataset_name}' not found in the configuration.")
    
    # Load the dataset using the datasets library
    if dataset_name == "stackoverflow":
        return _load_stackoverflow(dataset_info)
    elif dataset_name == "bingquery-logs":
        return _load_bingquery_logs(dataset_info)


def _load_stackoverflow(dataset_info: dict):
    # source from TDE-v2/benchmark-stackoverflow
    data = []
    
    for file in os.listdir(dataset_info["path"]):
        if file.endswith('.json'):
            json_fp = os.path.join(dataset_info["path"], file)
            with open(json_fp, 'r') as f:
                obj = json.load(f)
                obj['file_path'] = json_fp
                data.append(obj)

    return data

def _load_bingquery_logs(dataset_info: dict):
    # source from TDE-v2/benchmark-bingquery-logs: filter by prefix 'semantic_'
    data = []
    
    for file in os.listdir(dataset_info["path"]):
        if file.startswith('semantic_') and file.endswith('.json'):
            json_fp = os.path.join(dataset_info["path"], file)
            with open(json_fp, 'r') as f:
                obj = json.load(f)
                obj['file_path'] = json_fp
                data.append(obj)

    return data