# ChatTransform

## Overview
A LLM-powered data transformation tool
- [x] Chat-to-instruction: a fine-tuned weak model
- [x] Code Generation: a API-based strong model
- [ ] RAG: a retrieval-based transformation amendment

## Command Line Interface
1. Setup the vLLM endpoint for the fine-tuned model, model file should be stored in the `models` folder.
```bash
CUDA_VISIBLE_DEVICES=7 vllm serve ./models/llama3_lora_sft --config ./etc/vllm_serve.yaml
```

2. Run the experiment
```bash
python run.py --config etc/config_private.yaml --exp_name tde-stk
```