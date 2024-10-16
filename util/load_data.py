import json
    
DATASET_DICT = {
    "TDE-alpaca": {
        "path": "data/TDE-alpaca/tde-alpaca.json"
    }
}


def load_dataset_by_name(dataset_name):
    """Load the dataset based on the dataset_name from the configuration."""
    dataset_info = DATASET_DICT.get(dataset_name, None)
    if dataset_info is None:
        raise ValueError(f"Dataset '{dataset_name}' not found in the configuration.")
    
    # Load the dataset using the datasets library
    if dataset_name == "TDE-alpaca":
        return _load_tde_alpaca(dataset_info)


def _load_tde_alpaca(dataset_info: dict):
    # load json file
    with open(dataset_info["path"], "r") as f:
        data = json.load(f)
    return data

