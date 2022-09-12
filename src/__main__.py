'''
    Spreedsheet and Data Files Helper
'''
# standard


# third party


# local
from libs import arguments
from libs import utils


def run(keyargs):
    '''
    Run function, controls program functions and generates output files.

    Param
        - keyargs.excel_path (`String`): Excel path.
        - keyargs.output_path (`String`): Output directory path.
        - keyargs.dataset_type (`String`): Dataset name.
        - keyargs.metadata_sheet (`String`): Dataset sheet.
        - keyargs.rows_to_skip (`Integer`): Rows to skip.
    '''
    pass


if __name__ == '__main__':
    '''
    Main function Spreedsheet and Data Files Helper.
    Initializes variables for program execution.
    '''

    args = arguments.load_arguments()

    keyargs = {
        'excel_path': args.input,
        'output_path': args.output,
        'dataset_type': args.dataset_type,
        'metadata_sheet': args.sheet,
        'rows_to_skip': int(args.rows_to_skip)
    }
    utils.validate_directories(keyargs.get('output_path'))
    utils.validate_excel_file(keyargs.get('excel_path'))
    run(keyargs)
