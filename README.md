# MegaTran

## Overview
A LLM-powered framework that converts natural language queries into executable Python code for data transformation tasks. The system uses a two-stage approach:

1. **Weak2StrongPrompt**: Fine-tuned LLaMA model that converts natural language queries into articulated code instructions
2. **Prompt2Code**: GPT-4o based code generator that produces Python functions, with below two optimizations:
    - **Lazy-RAG (Retrieval-Augmented Generation)**: Code libraries retrieval system for third-party packages
    - **Sanity-check Reflection**: Sanity-check Reflection mechanism through error analysis

## Setup

1. Install dependencies
```bash
pip install -r requirements.txt
```

2. Configure environment variables
```bash
# Create .env file with your API keys
OPENAI_API_KEY=your_api_key_here
```

3. Start vLLM server for fine-tuned model
```bash
vllm serve \
    --model ./assets/models/llama3_lora_sft \ # after downloading ...
    --config ./etc/vllm-server.yaml
```
> Note: You can use `CUDA_VISIBLE_DEVICES` to specify the GPU device

4. Test weak2strong prompt inference
```bash
python w2s_prompt_inference.py -q "input:abc, output:ABC"

# Expected output: 
# format(): Convert the string to uppercase
```

5. [offline, optional] Build RAG vector database
```bash
# Build vector database for code libs retrieval
python scripts/build_vector_db.py \
    --config etc/vec_db.yaml \
    [-q "hijri date to gregorian date"] # test single query by adding this argument
```
> A pre-built vector database is saved in `assets/rag/code_db`


## Usage

1. Run the transformation pipeline
```bash
# Test mode (with smaller dataset)
python run.py \
    --config etc/mega-transform.yaml \
    --exp_name demo \
    --testing

# Full dataset run
python run.py \
    --config etc/mega-transform.yaml \
    --exp_name exp-1 \
    --dataset_name stackoverflow
```

2. Check experiment results as show in `demo` folder. Results will include:
- Code Generation Results (per task)
- Full test results (full_result.csv)
- Summary statistics (task-level accuracy, token usage, etc.)
- Runtime logs for current run


## Project Structure
```
chat-transform/
├── run.py                # Main execution script
├── w2s_prompt_inference.py # Weak2strong prompt inference
├── etc/                  # Configuration files
│   ├── mega-transform.yaml # pipeline config
│   ├── code-llm.yaml       # baseline Code LLM
│   ├── vllm-server.yaml    # vLLM server config
│   └── vec_db.yaml         # RAG vector database config
├── framework/            # Core components
│   ├── chat_to_inst.py   # Chat to instruction conversion
│   ├── code_generator.py # Code generation
│   ├── lazy_rag.py       # Lazy RAG module
│   ├── reflection.py     # Sanity-check Reflection module
│   └── prompt_generator.py # Prompt composition
├── util/                 # Utility modules
│   ├── analyzer.py       # Result analysis and reporting
│   ├── load_data.py      # Data loading utilities
│   ├── context_manager.py # Context management
│   └── __init__.py
├── assets/               # Model assets
│   ├── models/           # Fine-tuned models
│   └── rag/              # RAG related files (Vec DB, list of missing packages)
├── scripts/              # Utility scripts
│   ├── build_vector_db.py # Build RAG vector database
│   ├── foundation_model.py # Foundation model baseline
│   └── push_to_hf.py      # Push to HF
├── temp/                 # Temporary files (on-the-fly generated code)
├── .env                  # Environment variables
└── requirements.txt      # Project dependencies
```


## Baselines
Foundation model baseline, source code refer to  the orginal implementation [here](https://github.com/HazyResearch/fm_data_tasks/blob/main/notebooks/data_transformation_experiments.ipynb)
```bash
# Dataset: benchmark-stackoverflow
python scripts/foundation_model.py --dataset stackoverflow --model gpt-4o-mini

# Dataset: benchmark-BinqQuery (semantic)
python scripts/foundation_model.py --dataset bingquery-logs --model gpt-4o-mini
```
> you can specify the `model` parameter in line:44 to try other models


Naive code generation baseline:
```bash
python run.py \
    --config etc/code-llm.yaml \ # use code-llm config here
    --exp_name exp-1 \
    --dataset_name stackoverflow
```

## Download Model
The **Weak2StrongPrompt** Fine-tuning Model is avaliable at [HuggingFace](https://huggingface.co/Ti-ger/llama3_lora_dt_chat). Move the model files to `assets/models/`.

## License
[MIT License](LICENSE)
