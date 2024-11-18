# ChatTransform

## Overview
A LLM-powered framework that converts natural language queries into executable Python code for data transformation tasks. The system uses a multi-stage approach:

1. **Chat-to-Type**: Fine-tuned LLaMA model that predict the transformation type from user input and give the code instruction
2. **Code Generation**: Strong model (GPT-4) based code generator that produces Python functions
3. **RAG (Retrieval-Augmented Generation)**: Documentation lookup system for package APIs
4. **Reflection**: Self-improvement mechanism for code generation through error analysis

## Features
- [x] Natural language to code transformation
- [x] Multi-stage pipeline with specialized models
- [x] Automated package documentation retrieval
- [x] Error handling and code improvement through reflection
- [x] Support for various data transformation tasks
- [x] Parallel processing with thread safety

## Setup

1. Install dependencies
```bash
pip install -r requirements.txt
```

2. Configure OpenAI API
```yaml
# etc/config_template.yaml
openai_cfg:
  api_key: YOUR_API_KEY
  base_url: "https://api.openai.com/v1"
  model: "gpt-4"
```

3. Build RAG vector database
```bash
# Build vector database for package documentation
python build_vector_db.py \
    --config etc/config_template.yaml \
```
> --query "import statement" # test by adding this argument

4. Start vLLM endpoint for chat-to-instruction model
```bash
# Start vLLM server for fine-tuned model
vllm serve \
    --model ./assets/models/llama3_lora_sft \
    --config ./etc/vllm_serve.yaml
```
> Note: You can use `CUDA_VISIBLE_DEVICES` to specify the GPU device

## Usage

1. Run experiment
```bash
# Full dataset run
python run.py \
    --config etc/config_template.yaml \
    --exp_name stk-demo \
    --dataset_name stackoverflow

# Test run with subset
python run.py \
    --config etc/config_template.yaml \
    --exp_name test_run \
    --testing
```

2. Check experiment results
```
exp/
└── {exp_name}/
    ├── code/              # Generated Python code
    ├── result/
    │   ├── full_result.csv    # Detailed test results
    │   └── summary.json       # Experiment summary
    └── {exp_name}.log    # Experiment log
```

## Project Structure
```
ChatTransform/
├── run.py              # Main execution pipeline
├── build_vector_db.py  # RAG database builder
├── framework/            # Core components
│   ├── chat_to_type.py  # Chat to type prediction
│   ├── code_generator.py # Code generation and execution
│   ├── lazy_rag.py      # Package documentation retrieval
│   ├── reflection.py    # Code improvement mechanism
│   └── analysis.py      # Result analysis
├── util/                # Utility modules
├── assets/              # Resource files
│   └── rag/
│       ├── pkg_info.json   # Package documentation info
│       └── vector_db/      # FAISS vector database
├── data/                # Transformation datasets
│   └── TDE-v2/         # Benchmark dataset
├── etc/                 # Configuration files
│   ├── config_template.yaml  # Configuration template
│   └── vllm_serve.yaml      # vLLM server config
├── exp/                 # Experiment outputs
└── temp/               # Temporary files
```

## Configuration Options
Key settings in `config_template.yaml`:
```yaml
chat_to_type: true           # Enable chat-to-type
n_shot: 3                    # Number of examples to use for code generation
code_retry: 3                # Max code generation retries
prompt_mode: "chat_example"  # Prompt composition mode
```

## License
[MIT License](LICENSE)