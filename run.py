import argparse
from tqdm import tqdm
from util import load_dataset_by_name, Context
from framework import ChatBuilder, CodeGenerator, ResultAnalyzer


def main(ctx):
     # Load the dataset based on the dataset_name
    ctx.logger.info(f"Loading dataset {ctx.dataset_name}...")
    dataset = load_dataset_by_name(ctx.dataset_name)
    
    # uncomment for testing
    # dataset = dataset[:5]

    if ctx.get('chat_to_inst', False):  # Use False as default if key doesn't exist
        # chat-to-instruction
        chatBuilder = ChatBuilder(dataset, ctx)
        dataset = chatBuilder.run()

    # Inference Code Per test case and evaluate result with Analyzer
    resultAnalyzer = ResultAnalyzer(ctx)
    codeGen = CodeGenerator(ctx)

    for item in tqdm(dataset, desc="Processing test cases"):
        tests = codeGen.run(item)
        resultAnalyzer.add_record(item['file_path'], tests)

    # Save output to file
    resultAnalyzer.export_csv_full_result()
    resultAnalyzer.export_json_summary()

    return


if __name__ == '__main__':
    
    # Argument parser
    parser = argparse.ArgumentParser(description='Run experiment')
    parser.add_argument('--exp_name', default='demo', type=str, help='unique to current experiment')
    parser.add_argument('--dataset_name', required=True, type=str, help='dataset name, refer to util/load_data.py, DATASET_DICT')
    parser.add_argument('--config', default='./etc/config_template.yaml', type=str, help='path to config file')
    
    args = parser.parse_args()

    # Setup experiment context
    ctx = Context(args) 
    main(ctx)
