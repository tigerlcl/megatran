import os
import json
from typing import List, Dict


def get_project_root():
    current_file = os.path.abspath(__file__)
    return os.path.dirname(os.path.dirname(current_file))

DATASET_DICT = {
    "stackoverflow": {
        "path": os.path.join(get_project_root(), "data/TDE-v2/benchmark-stackoverflow")
    },
    "bingquery-logs": {
        "path": os.path.join(get_project_root(), "data/TDE-v2/benchmark-bing-query-logs")
    },
    "unit_convert": {
        "path": os.path.join(get_project_root(), "data/TDE-v2/benchmark-bing-query-logs")
    },
    "headcase": {
        "path": os.path.join(get_project_root(), "data/TDE-v2/benchmark-headcase")
    },
    "prep-software": {
        "path": os.path.join(get_project_root(), "data/TDE-v2/benchmark-FF-Trifacta-GoogleRefine")
    },
    "DTT-variant": {
        "path": os.path.join(get_project_root(), "data/DTT-variant/")
    },
    "Manual": {
        "path": os.path.join(get_project_root(), "data/Manual")
    },
    "Science": {
        "path": os.path.join(get_project_root(), "data/Science")
    },
    "test-data": {
        "path": os.path.join(get_project_root(), "data/testset/")
    }
}

# Datasets using standard JSON format
JSON_NORMAL_GROUP = [
    "stackoverflow", "headcase", "prep-software", 
    "DTT-variant", "Manual", "Science",
    "test-data"
    ]

def load_dataset_by_name(dataset_name: str) -> List[Dict]:
    """Load dataset based on name from configuration"""
    dataset_info = DATASET_DICT.get(dataset_name)
    if dataset_info is None:
        raise ValueError(f"Dataset '{dataset_name}' not found in configuration")
    
    # Load dataset based on type
    if dataset_name in JSON_NORMAL_GROUP:
        dataset = _load_json_files(dataset_info)
    elif dataset_name == "bingquery-logs":
        dataset = _load_bingquery_logs(dataset_info)
    elif dataset_name == "unit_convert":
        dataset = _load_unit_convert(dataset_info)

    # Sort by file path for consistent ordering
    return sorted(dataset, key=lambda x: x['file_path'])

def _load_json_files(dataset_info: dict):
    data = []
    for file in os.listdir(dataset_info["path"]):
        if file.endswith('.json'):
            json_fp = os.path.join(dataset_info["path"], file)
            with open(json_fp, 'r') as f:
                obj = json.load(f)
                obj['file_path'] = json_fp # store file path for logging
                data.append(obj)

    return data

def _load_bingquery_logs(dataset_info: dict):
    """source from TDE-v2/benchmark-bingquery-logs: filter by prefix 'semantic_"""
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
    """source from TDE-v2/benchmark-bing-query-logs: filter by prefix 'unit_'"""
    data = []
    
    for file in os.listdir(dataset_info["path"]):
        if file.startswith('unit_') and file.endswith('.json'):
            json_fp = os.path.join(dataset_info["path"], file)
            with open(json_fp, 'r') as f:
                obj = json.load(f)
                obj['file_path'] = json_fp
                data.append(obj)

    return data
