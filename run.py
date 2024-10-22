import os
import argparse

from util import Context, load_dataset_by_name
from framework import ChatBuilder, CodeGenerator, ResultAnalyzer


def main(ctx):
     # Load the dataset based on the dataset_name
    ctx.logger.info("Loading dataset...")
    dataset = load_dataset_by_name(ctx.dataset_name)

    # get subset for testing
    dataset = dataset[:5]

    resultAnalyzer = ResultAnalyzer()

    # chat-to-instruction
    chatBuilder = ChatBuilder(dataset, ctx)
    dataset = chatBuilder.run()

    # Inference Code and evaluate result
    codeGen = CodeGenerator(ctx)
    for item in dataset:
        tests = codeGen.run(item)
        resultAnalyzer.add_record(item['file_path'], tests)

    # Save output to file
    csv_fp = os.path.join(ctx.result_dir, 'full_result.csv')
    resultAnalyzer.export_from_dataframe(csv_fp)

    summary = resultAnalyzer.get_stat()
    ctx.logger.info(summary)

    summary_json_fp = os.path.join(ctx.result_dir, 'summary.json')
    resultAnalyzer.export_stat(summary_json_fp)

    return


if __name__ == '__main__':
    
    # Argument parser
    parser = argparse.ArgumentParser(description='Run experiment')
    parser.add_argument('--exp_name', default='demo', type=str, help='unique to current experiment')
    parser.add_argument('--config', default='./etc/config_private.yaml', type=str, help='path to config file')

    args = parser.parse_args()

    # Setup experiment context
    ctx = Context(args) 
    main(ctx)
