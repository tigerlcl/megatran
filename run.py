import argparse
from tqdm import tqdm
from util import load_dataset_by_name, Context
from framework import ChatBuilder, CodeGenerator, ResultAnalyzer

def main(ctx: Context) -> None:
    """
    Main execution pipeline for the ChatTransform experiment
    
    Workflow:
    1. Load dataset
    2. (Optional) Convert chat to instruction using fine-tuned model
    3. Generate and test code for each item
    4. Analyze and export results

    """
    # Load and prepare dataset
    ctx.logger.info(f"Loading dataset {ctx.dataset_name}...")
    dataset = load_dataset_by_name(ctx.dataset_name)
    
    # Use subset for testing if specified
    if ctx.testing:
        ctx.logger.info("Running in test mode with subset of data")
        dataset = dataset[:5]

    # Optional: Convert natural language to formal instruction
    if ctx.get('chat_to_inst', False):
        ctx.logger.info("Converting chat to instruction format...")
        chat_builder = ChatBuilder(dataset, ctx)
        dataset = chat_builder.run()
        ctx.logger.info("Chat conversion completed")

    # Initialize components
    result_analyzer = ResultAnalyzer(ctx)
    code_generator = CodeGenerator(ctx)

    # Process each test case
    ctx.logger.info("Starting code generation and testing...")
    for item in tqdm(dataset, desc="Processing test cases"):
        # Generate and test code
        tests = code_generator.run(item)
        # Record results
        result_analyzer.add_record(item['file_path'], tests)

    # Export results
    ctx.logger.info("Exporting results...")
    result_analyzer.export_csv_full_result()
    result_analyzer.export_json_summary()
    
    ctx.logger.info("Experiment completed successfully")


if __name__ == '__main__':
    try:
        # Parse command line arguments
        parser = argparse.ArgumentParser(
            description='Run ChatTransform experiment',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter
        )
        
        parser.add_argument('--exp_name', default='demo', type=str, help='Unique experiment name')
        parser.add_argument('--dataset_name', required=True, type=str, help='Dataset name from load_data.py/DATASET_DICT')
        parser.add_argument('--config', default='./etc/config_template.yaml', type=str, help='Path to config file')
        parser.add_argument('--testing', action='store_true', help='Run on small subset of data for testing')
        
        args = parser.parse_args()
        
        # Setup experiment context and run
        ctx = Context(args)
        main(ctx)
        
    except Exception as e:
        # Log any unhandled exceptions
        if 'ctx' in locals() and hasattr(ctx, 'logger'):
            ctx.logger.error(f"Experiment failed: {str(e)}", exc_info=True)
        raise
