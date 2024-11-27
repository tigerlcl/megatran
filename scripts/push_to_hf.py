import os
from dotenv import load_dotenv
from huggingface_hub import HfApi

load_dotenv()

if __name__ == "__main__":
    # Define your model path and repository name
    model_path = '../assets/models/llama3_lora_sft'
    repo_name = os.getenv("MODEL_REPO")
    
    api = HfApi(token=os.getenv("HF_TOKEN"))
    if not api.repo_exists(repo_name):
        api.create_repo(repo_name)

    # Upload the model
    api.upload_folder(
        folder_path=model_path,
        repo_id=repo_name,
        commit_message="Initial model upload"
    )
