import os
import sys
import importlib
import argparse
from tqdm import tqdm

# sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from util import load_data

from config.context_manager import Context
from framework.synthesize import InstructionBuilder
from framework.code_gen import CodeGenerator
from framework.analysis import ResultAnalyzer


def main(ctx):
     # Load the dataset based on the dataset_name
    ctx.logger.info("Loading dataset...")
    dataset = load_data.load_dataset_by_name(ctx.dataset_name) 

    resultAnalyzer = ResultAnalyzer()

    # TODO: Refine below code
    for f in tqdm(dataset):
        test_fp = f['file_path']  
        ctx.logger.info(f"Processing {test_fp}")

        instBuilder = InstructionBuilder(inst_fp, test_fp)
        instruction = instBuilder.run()
        test_data = instBuilder.load_test_data()
        ctx.logger.info(f"Instruction: {instruction}")

        # Run OpenAI inference and generate code
        py_fn = f.replace('.txt', '.py')
        py_fp = f"{ctx.code_dir}/{py_fn}"
        codeGen = CodeGenerator(ctx.cfg["llm"])
        codeExist, llm_cost = codeGen.run(instruction, py_fp)
        ctx.logger.info(f"Code Gen LLM cost: {llm_cost}")

        # Execute code and evaluate result
        if codeExist:
            try:
                temp = importlib.reload(temp)  # Reload auto-generated module
            except Exception as e:
                ctx.logger.error(f"Error when importing code: {e}")
                continue  # Skip if code failed

            for test in test_data:
                try:
                    res = temp.solution(test[0])
                except Exception as e:
                    ctx.logger.error(f"Error when running code: {e}")
                    res = None
                test.append(res)

            # Add code execution result
            resultAnalyzer.add_record(test_fp, test_data)
        else:
            ctx.logger.info(f"Code not found, continue to next")

    # Save output to file
    resultAnalyzer.to_df()
    resultAnalyzer.export(csv_fp=f"{ctx.result_dir}/{ctx.exp_name}.csv")
    ctx.logger.info(resultAnalyzer.get_stat())

    return


if __name__ == '__main__':
    
    # Argument parser
    parser = argparse.ArgumentParser(description='Run experiment')
    parser.add_argument('--exp_name', type=str, default='demo', help='unique to current experiment')
    parser.add_argument('--dataset_name', type=str, required=True, help='name of the dataset, refer to util/load_data.py, DATASET_DICT')
    parser.add_argument('--config', type=str, default='./etc/config_private.yaml', help='path to config file')

    args = parser.parse_args()

    # Setup experiment context
    ctx = Context(args) 

    main(ctx)
