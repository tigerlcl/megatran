import os
import sys
import argparse
import logging
import time
import json

from openai import OpenAI
from dotenv import load_dotenv

# Add project root to path (temporary for this session only)
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from util import load_dataset_by_name, compare_values

def run(dataset: list, client: OpenAI, logger: logging.Logger) -> None:
    """Run the foundation model baseline"""

    n_shot=3
    accuracy = []
    token_cost = []
    results_log = []

    output_file = f"results/FM/{args.model}_{args.dataset}.json"

    logger.info(f"Processing dataset with {len(dataset)} items")
    for idx, item in enumerate(dataset):
        logger.info(f"Processing item [{idx+1}/{len(dataset)}]: {item['file_path']}")

        # process tuples for each item
        instruction = item['chat'] + "\nOnly output the transformed result without any explanation.\n"
        # in-context learning (first n_shot examples)
        icl = "Examples:\n" + "\n".join([f"Input: {t['input']}\nOutput: {t['output']}" for t in item['tuples'][:n_shot]])

        sub_acc = []
        # iterate over the remaining examples
        for t in item['tuples'][n_shot:]:

            user_input = f"{instruction}\n\n{icl}\nBased on the above examples, please transform the following input: {t['input']}\noutput:"
            logger.info(f"User Input:\n{user_input}")

            # generate response
            time.sleep(0.5)
            response = client.chat.completions.create(
            model=args.model,
            messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ],
            temperature=0,
            max_completion_tokens=30 # as max_tokens deprecated
            )

            # check if the response is correct
            result = response.choices[0].message.content.strip()

            if type(t['output']) == str:
                ground_truth = t['output'].strip()
            else:
                ground_truth = t['output']

            # 记录当前结果
            current_result = {
                'file_path': item['file_path'],
                'input': t['input'],
                'output': result,
                'ground_truth': ground_truth,
                'is_correct': 'True' if compare_values(result, ground_truth) else 'False',
                'instruction': instruction,
                'examples': icl
            }
            results_log.append(current_result)

            # 新增：立即保存当前结果
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(results_log, f, ensure_ascii=False, indent=2)

            logger.info(f"Output: {result}")
            logger.info(f"Results updated in {output_file}\n")

            # store token cost: (prompt, completion)
            token_cost.append((response.usage.prompt_tokens, response.usage.completion_tokens))

            if compare_values(result, ground_truth):
                sub_acc.append(1)
            else:
                sub_acc.append(0)

        # calculate accuracy for this item
        if len(sub_acc) == sum(sub_acc):
            accuracy.append(1)
        else:
            accuracy.append(0)

    logger.info(f"Final accuracy on {args.dataset}: {sum(accuracy) / len(accuracy)}")

    # calculate average token cost
    avg_prompt_cost = sum([t[0] for t in token_cost]) / len(token_cost)
    avg_completion_cost = sum([t[1] for t in token_cost]) / len(token_cost)
    logger.info(f"Average token costs - prompt: {int(avg_prompt_cost)}, completion: {int(avg_completion_cost)}")

    # 最终日志信息
    logger.info(f"All results saved to {output_file}")

    return


if __name__ == "__main__":
    load_dotenv()

    parser = argparse.ArgumentParser(description="Run the foundation model pipeline")
    parser.add_argument('--dataset', type=str, help='Dataset to use')
    parser.add_argument('--model', type=str, help='Model to use, refer to OpenAI Models')
    args = parser.parse_args()

    # stackoverflow and bingquery-logs (semantic)
    dataset = load_dataset_by_name(args.dataset)
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_BASE_URL")
    )

    # setup logging
    logging.basicConfig(
        level=logging.INFO,
        handlers=[
            logging.FileHandler(f"results/FM/fm_{args.dataset}_{args.model}.log", mode='w'),
            logging.StreamHandler()  # This will output to console
        ]
    )
    logger = logging.getLogger('fm-baseline')
    logger.info(f"Running Foundation Model on {args.dataset}")

    run(dataset, client, logger)
