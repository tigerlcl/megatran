import argparse
from openai import OpenAI

def main(query: str):
    vllm_client = OpenAI(base_url="http://localhost:8000/v1", api_key="token-abc123")
    model_path = './assets/models/llama3_lora_sft'
    try:
        completion = vllm_client.chat.completions.create(
            model=model_path,
            messages=[{"role": "user", "content": query}],
            temperature=0.2
        )
    except Exception as e:
        raise RuntimeError(f"Failed to connect to the vLLM client, please check your config.")
    
    inst = completion.choices[0].message.content
    print(inst)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Weak2strong prompt inference")
    parser.add_argument("--query", '-q', type=str, required=True, help="Query for weak2strong prompt inference")
    args = parser.parse_args()

    main(args.query)
    