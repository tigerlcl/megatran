import os
import sys
import yaml
import importlib
import argparse
import logging
from tqdm import tqdm

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from util.synthesize import InstructionBuilder
from util.code_gen import CodeGenerator
from util.analysis import ResultAnalyzer


def main():
    # load dataset
    logging.info("Loading dataset")
    files = [f for f in os.listdir(dataset_dir) if f.endswith(".txt")]
    # Sort the list using the numeric part of the filenames
    sorted_list = sorted(files, key=lambda x: int(x.split('.')[0]))
    resultAnalyzer = ResultAnalyzer()

    # sorted_list = ['1.txt', '2.txt', '3.txt'] # for debug
    # sorted_list = ['5.txt']
    for f in tqdm(sorted_list[:10]):
        test_fp = os.path.join(dataset_dir, f)
        inst_fp = os.path.join(cfg["instruction_dir"], args.dataset, f)
        logging.info(f"Processing {test_fp}")

        # build prompt per sample with N shots, N=0,1,2
        instBuilder = InstructionBuilder(inst_fp, test_fp, args.shot)
        instruction = instBuilder.run()
        test_data = instBuilder.load_test_data()

        # run OpenAI inference and generate code
        py_fn = f.replace('.txt', '.py')
        py_fp = f"{code_dir}/{py_fn}"
        codeGen = CodeGenerator(cfg["llm"])
        codeExist, llm_cost = codeGen.run(instruction, py_fp)
        logging.info(f"Code Gen LLM cost: {llm_cost}")

        # exec code and evaluate result
        if codeExist:
            import temp_solve
            importlib.reload(temp_solve)  # reload auto-generated module
            for test in test_data:
                try:
                    res = temp_solve.solution(test[0])
                except Exception as e:
                    # logging.error(f"Error when running code: {e}")
                    res = None
                test.append(res)

            # add code execution result
            resultAnalyzer.add_record(test_fp, test_data)
        else:
            logging.info(f"Code not found, continue to next")

    # save output to file
    resultAnalyzer.to_df()
    resultAnalyzer.export(csv_fp=f"{result_dir}/{args.exp_name}.csv")
    logging.info(resultAnalyzer.get_stat())

    return


if __name__ == '__main__':
    # Get the parent directory of the current script
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(parent_dir)

    # argument parser
    parser = argparse.ArgumentParser(description='Run the main function')
    parser.add_argument('--exp_name', type=str, default='demo', help='experiment name')
    parser.add_argument('--dataset', type=str, default='demo', help='path to dataset')
    parser.add_argument('--shot', type=int, default=0, help='number of example shots')

    args = parser.parse_args()

    # Configure the logger
    logging.basicConfig(filename=f'log/{args.exp_name}.log',
                        filemode='w',
                        level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    # Load config
    with open('etc/config_private.yaml', 'r') as file:
        cfg = yaml.safe_load(file)

    # check dirs
    dataset_dir = f"{cfg['dataset_dir']}/{args.dataset}"
    if not os.path.exists(dataset_dir):
        raise FileNotFoundError(f"Dataset directory {dataset_dir} not found")

    code_dir = os.path.join(cfg["code_dir"], args.exp_name)
    if not os.path.exists(code_dir):
        os.makedirs(code_dir)

    result_dir = cfg["result_dir"]
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)

    main()
