import os
import sys
import argparse
import logging
import time

from openai import OpenAI
from dotenv import load_dotenv

# Add project root to path (temporary for this session only)
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from util import load_dataset_by_name, compare_values

load_dotenv()

def run(dataset: list, client: OpenAI, logger: logging.Logger) -> None:
    """Run the foundation model baseline"""

    n_shot=3
    accuracy = []
    token_cost = []

    logger.info(f"Processing dataset with {len(dataset)} items")
    for idx, item in enumerate(dataset):
        logger.info(f"Processing item [{idx+1}/{len(dataset)}]: {item['file_path']}")

        # process tuples for each item
        instruction = item['chat']
        # in-context learning (first n_shot examples)
        icl = "\n".join([f"Input: {t['input']}\nOutput: {t['output']}" for t in item['tuples'][:n_shot]])

        sub_acc = []
        # iterate over the remaining examples
        for t in item['tuples'][n_shot:]:

            user_input = f"{instruction}\n\n{icl}\ninput: {t['input']}\noutput:\n\nreturn the output value only"
            logger.info(f"User Input:\n{user_input}")

            # generate response
            time.sleep(0.5)
            response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ],
            temperature=0,
            max_completion_tokens=30 # as max_tokens deprecated
            )

            # check if the response is correct
            result = response.choices[0].message.content.strip()
            logger.info(f"Output: {result}\n")
            # store token cost: (prompt, completion)
            token_cost.append((response.usage.prompt_tokens, response.usage.completion_tokens))

            if compare_values(result, t['output']):
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

    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the foundation model pipeline")
    parser.add_argument('--dataset', type=str, help='Dataset to use')
    args = parser.parse_args()

    # stackoverflow and bingquery-logs (semantic)
    dataset = load_dataset_by_name(args.dataset)
    client = OpenAI()

    # setup logging
    logging.basicConfig(
        level=logging.INFO,
        handlers=[
            logging.FileHandler(f"scripts/fm_{args.dataset}.log", mode='w'),
            logging.StreamHandler()  # This will output to console
        ]
    )
    logger = logging.getLogger('fm-baseline')
    logger.info(f"Running Foundation Model on {args.dataset}")

    run(dataset, client, logger)
