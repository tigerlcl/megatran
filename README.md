# MegaTran

## Overview
A LLM-powered framework that converts natural language queries into executable Python code for data transformation tasks. The system uses a two-stage approach:

1. **Weak2StrongPrompt**: Fine-tuned LLaMA model that converts natural language queries into structured code instructions
2. **Prompt2Code**: GPT-4 based code generator that produces Python functions
3. **Lazy-RAG (Retrieval-Augmented Generation)**: Documentation lookup system for package APIs
4. **Sanity-check Reflection**: Sanity-check Reflection mechanism for code generation through error analysis

## Features
- [x] Natural language to code transformation
- [x] Multi-stage pipeline with specialized models
- [x] Automated package documentation retrieval
- [x] Error handling and code improvement through reflection
- [x] Support for various data transformation tasks (unit conversion, text formatting, etc.)
- [x] Comprehensive result analysis and reporting

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

3. Build RAG vector database
```bash
# Build vector database for package documentation
python scripts/build_vector_db.py \
    --config etc/vec_db.yaml \
    [-q "hijri date to gregorian date"] # test single query by adding this argument
```

4. Start vLLM server for fine-tuned model
```bash
vllm serve \
    --model ./assets/models/llama3_lora_sft \
    --config ./etc/vllm-server.yaml
```
> Note: You can use `CUDA_VISIBLE_DEVICES` to specify the GPU device

5. Test chat-to-inst inference
```bash
python chat_to_inst_inference.py -q "input:abc, output:ABC"
```

## Usage

1. Run the transformation pipeline
```bash
# Full dataset run
python run.py \
    --config etc/mega-transform.yaml \
    --exp_name stk-demo \
    --dataset_name stackoverflow

# Test run (with smaller dataset)
python run.py \
    --config etc/mega-transform.yaml \
    --exp_name test_run \
    --testing
```

2. Check experiment results
```
Results will include:
- Full test results (full_result.csv)
- Summary statistics (task-level accuracy, token usage, etc.)
```

## Project Structure
```
chat-transform/
├── run.py                # Main execution script
├── chat_to_inst_inference.py # Chat-to-inst inference
├── etc/                  # Configuration files
│   ├── mega-transform.yaml # pipeline config
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
│   └── rag/              # RAG related files
├── scripts/              # Utility scripts
│   ├── build_vector_db.py # Build RAG vector database
│   ├── foundation_model.py # Foundation model baseline
│   └── push_to_hf.py      # Push to HF
├── temp/                 # Temporary files (on-the-fly generated code)
├── .env                  # Environment variables
└── requirements.txt      # Project dependencies
```


## Baseline
Foundation model baseline, [link](https://github.com/HazyResearch/fm_data_tasks/blob/main/notebooks/data_transformation_experiments.ipynb)
```bash
# Dataset: benchmark-stackoverflow
python scripts/foundation_model.py --dataset stackoverflow

# Dataset: benchmark-BinqQuery (semantic)
python scripts/foundation_model.py --dataset bingquery-logs
```

## Download model
The **Weak2StrongPrompt** Fine-tuning Model is avaliable at [HuggingFace](https://huggingface.co/Ti-ger/llama3_lora_dt_chat)

## License
[MIT License](LICENSE)
