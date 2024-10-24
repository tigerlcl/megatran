import os
import json
    
DATASET_DICT = {
    "stackoverflow": {
        "path": "./data/TDE-v2/benchmark-stackoverflow"
    },
    "bingquery-logs": {
        "path": "./data/TDE-v2/benchmark-bing-query-logs"
    },
    "unit_convert": {
        "path": "./data/TDE-v2/benchmark-bing-query-logs"
    },
    "headcase": {
        "path": "./data/TDE-v2/benchmark-headcase"
    },
    "prep-software": {
        "path": "./data/TDE-v2/benchmark-FF-Trifacta-GoogleRefine"
    }
}

# for non-special datasets, the data is stored in json files
JSON_NORMAL_GROUP = ["stackoverflow", "headcase", "prep-software"]


def load_dataset_by_name(dataset_name):
    """Load the dataset based on the dataset_name from the configuration."""

    dataset_info = DATASET_DICT.get(dataset_name, None)
    if dataset_info is None:
        raise ValueError(f"Dataset '{dataset_name}' not found in the configuration.")
    
    # Load the dataset using the datasets library
    if dataset_name in JSON_NORMAL_GROUP:
        dataset =  _load_json_files(dataset_info)
    elif dataset_name == "bingquery-logs":
        dataset = _load_bingquery_logs(dataset_info)
    elif dataset_name == "unit_convert":
        dataset = _load_unit_convert(dataset_info)

    # sort dataset by file_path
    dataset = sorted(dataset, key=lambda x: x['file_path'])

    return dataset

def _load_json_files(dataset_info: dict):
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

def _load_unit_convert(dataset_info: dict):
    # source from TDE-v2/benchmark-unit-convert: filter by prefix 'semantic_'
    data = []
    
    for file in os.listdir(dataset_info["path"]):
        if file.startswith('unit_') and file.endswith('.json'):
            json_fp = os.path.join(dataset_info["path"], file)
            with open(json_fp, 'r') as f:
                obj = json.load(f)
                obj['file_path'] = json_fp
                data.append(obj)

    return data
