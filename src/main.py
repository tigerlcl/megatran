import os
import yaml
import logging

from util.synthesize import InstructionBuilder
from util.code_gen import CodeGenerator
from util.analysis import ResultAnalyzer


def main():
    # load dataset
    logging.info("Loading dataset")
    test_dir = cfg["test_data_dir"]
    files = [f for f in os.listdir(test_dir) if f.endswith(".txt")]
    # Sort the list using the numeric part of the filenames
    sorted_list = sorted(files, key=lambda x: int(x.split('.')[0]))
    n_shot = 2  # parameter

    result = ResultAnalyzer(cfg["result_dir"], n_shot)

    sorted_list = ['1.txt', '2.txt', '3.txt']
    for f in sorted_list:
        test_fp = os.path.join(test_dir, f)
        inst_fp = os.path.join(cfg["instruction_dir"], f)
        logging.info(f"Processing {test_fp}")

        # build prompt per sample with N shots, N=0,1,2
        instBuilder = InstructionBuilder(inst_fp, test_fp, n_shot)
        instruction = instBuilder.run()
        # logging.info(instruction)

        test_data = instBuilder.load_test_data()

        # run OpenAI inference and generate code
        py_fp = os.path.join(cfg["code_dir"], f.replace(".txt", ".py"))
        codeGen = CodeGenerator(cfg["llm"])
        codeExist, llm_cost = codeGen.run(instruction, py_fp)
        logging.info(f"Code Gen LLM cost: {llm_cost}")

        # exec code and evaluate result
        if codeExist:
            logging.info(f"Evaluating result")
            from temp_solve import solution
            for test in test_data:
                try:
                    res = solution(test[0])
                except Exception as e:
                    logging.error(f"Error when running code: {e}")
                    res = None
                test.append(res)

            # add code execution result
            result.add_record(test_fp, test_data)
        else:
            logging.info(f"Code not found, continue to next")

    # save output to file
    result.export()
    logging.info(result.get_stat())

    return


if __name__ == '__main__':
    # Get the parent directory of the current script
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(parent_dir)

    # Configure the logger
    logging.basicConfig(filename='./log/run.log',
                        level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    # Load config
    with open('etc/config_private.yaml', 'r') as file:
        cfg = yaml.safe_load(file)

    main()
