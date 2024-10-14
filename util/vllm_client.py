from openai import OpenAI

def vllm_chat(prompt):
    """
    vLLM provides an HTTP server that implements OpenAI’s Completions and Chat API.

    """
    client = OpenAI(
        base_url="http://localhost:8000/v1",
        api_key="token-abc123",
    )

    completion = client.chat.completions.create(
        model="/home/lichanglun/LLaMA-Factory/models/llama3_lora_sft",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    # Access the content attribute directly
    res = completion.choices[0].message.content
    
    return res

if __name__ == "__main__":
    
    # Example usage of OpenAI chat
    chat = "transform unix timestamp to human readable date"
    res = vllm_chat(chat)
    print(res)
