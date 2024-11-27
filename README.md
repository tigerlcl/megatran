# ChatTransform

## Overview
A LLM-powered framework that converts natural language queries into executable Python code for data transformation tasks. The system uses a multi-stage approach:

1. **Chat-to-Instruction**: Fine-tuned LLaMA model that converts natural language queries into structured code instructions
2. **Code Generation**: GPT-4 based code generator that produces Python functions
3. **RAG (Retrieval-Augmented Generation)**: Documentation lookup system for package APIs
4. **Reflection**: Self-improvement mechanism for code generation through error analysis

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
python build_vector_db.py \
    --config etc/vec_db.yaml \
    [--query "xxxx"] # test single query by adding this argument
```

4. Start vLLM endpoint for chat-to-instruction model
```bash
# Start vLLM server for fine-tuned model
vllm serve \
    --model ./assets/models/llama3_lora_sft \
    --config ./etc/vllm-server.yaml
```
> Note: You can use `CUDA_VISIBLE_DEVICES` to specify the GPU device

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
├── temp/                 # Temporary files (on-the-fly generated code)
├── .env                  # Environment variables
└── requirements.txt      # Project dependencies
```

Key settings in `etc/mega-transform.yaml`:
Turn on/off relevant module:
- `chat_to_inst`: true
- `allow_reflection`: true
- `allow_rag`: true


## Baseline
Foundation model baseline, [link](https://github.com/HazyResearch/fm_data_tasks/blob/main/notebooks/data_transformation_experiments.ipynb)
```bash
python scripts/foundation_model.py --dataset stackoverflow
```

## License
[MIT License](LICENSE)