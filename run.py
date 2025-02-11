import argparse
from time import perf_counter
from datetime import timedelta

from util import load_dataset_by_name, Context
from framework import ChatBuilder, CodeGenerator


def mega_transform(ctx: Context, dataset: list) -> None:
    """Main  pipeline for the MegaTransform experiment"""

    # Predict transformation type from user input
    if ctx.chat_to_inst:
        chatBuilder = ChatBuilder(ctx)
    else:
        chatBuilder = None
    
    # Initialize Code generator
    code_generator = CodeGenerator(ctx)

    # Process each test case
    ctx.logger.info("Starting Experiment...")
    for idx, item in enumerate(dataset):
        ctx.logger.info(f"Task [{idx}] Processing {item['file_path']}...")
        if chatBuilder:
            item = chatBuilder.run(item)

        # Generate and test code (Sanity-check Reflection + Lazy-RAG)
        tests = code_generator.run(item)

        # Record results
        ctx.logger.info(f"Task [{idx}] final results: {tests}")
        pass_cnt = ctx.result_analyzer.add_record(item['file_path'], tests)
        if pass_cnt > 0 and pass_cnt == len(tests):
            ctx.logger.info(f"All {len(tests)} test cases passed")
        else:
            ctx.logger.info(f"Passed {pass_cnt}/{len(tests)} test cases")

    return

def main(ctx: Context) -> None:
    """
    Main execution pipeline for the MegaTransform experiment
    
    Workflow:
    1. Load dataset
    2. Predict transformation type from user input
    3. Generate and test code for each task
    4. Analyze and export results

    """
    # Load and prepare dataset
    if ctx.testing:
        ctx.logger.info("Running in test mode with testing data")
        dataset = load_dataset_by_name("test-data")
    else:
        ctx.logger.info(f"Loading dataset {ctx.dataset_name}...")
        dataset = load_dataset_by_name(ctx.dataset_name)

    # set timer
    start_time = perf_counter()

    # run mega-transform pipeline
    mega_transform(ctx, dataset)

    # Export results
    ctx.logger.info("Exporting results...")
    csv_fp = ctx.result_analyzer.export_csv_full_result()
    ctx.logger.info(f"Full result exported to {csv_fp}")
    
    json_fp, test_stats, token_stats = ctx.result_analyzer.export_json_summary()
    ctx.logger.info(f"Summary exported to {json_fp}, Test stats: {test_stats}, Token stats: {token_stats}")

    duration = perf_counter() - start_time
    ctx.logger.info(f"Experiment completed successfully. Duration: {timedelta(minutes=duration//60, seconds=duration%60)}")


if __name__ == '__main__':

    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description='Run main experiment',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument('--exp_name', default='demo', type=str, help='Unique experiment name')
    parser.add_argument('--dataset_name', type=str, help='Dataset name from load_data.py/DATASET_DICT')
    parser.add_argument('--config', required=True, type=str, help='Path to config file')
    parser.add_argument('--model', default="gpt-4o-mini", required=True, type=str, help='LLM backend model name')
    parser.add_argument('--testing', action='store_true', help='Run on small subset of data for testing')
    
    args = parser.parse_args()
    
    # Setup experiment context
    ctx = Context(args)
    main(ctx)

