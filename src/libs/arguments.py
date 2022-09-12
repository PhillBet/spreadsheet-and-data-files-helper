'''
    ARGUMENTS
'''
# standard
import argparse

# third party


# local


def get_arguments():
    '''
    Defines the arguments that the program will support.

    Returns
        - arguments (`argparse Object`): defined arguments for the execution of the program.
    '''

    # ARGUMENTS DESCRIPTION

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="Database Metadata",
        epilog="You need to provided at least one entity argument")

    # GENERAL ARGUMENTS

    parser.add_argument(
        "-l",
        "--log",
        help="Path where the log of the process will be stored.",
        metavar="./logs/",
        default="./logs/",
    )

    parser.add_argument(
        "-r",
        "--report",
        help="Path where the report of the process will be stored.",
        metavar="../logs/ht_etl_log/",
        default="../logs/ht_etl_log/",
    )

    parser.add_argument(
        "-dstype",
        "--dataset-type",
        help="Dataset record source name.",
        choices=["TFBINDING", "GENE_EXPRESSION",
                 "TSS", "TUS", "TTS", "REGULONS", "GSELEX"],
        default="TFBINDING"
    )

    # FILES ARGUMENTS

    parser.add_argument(
        "-in",
        "--input",
        help="Path to read de origin file data.",
        metavar="Data/InputData/XLSX_example.xlsx",
        default="Data/InputData/XLSX_example.xlsx",
    )

    parser.add_argument(
        "-out",
        "--output",
        help="Path where the processed json files will be stored.",
        metavar="Data/RawData/",
        default="Data/RawData/",
    )

    parser.add_argument(
        "-sheet",
        "--sheet",
        help="Sheet from the Excel file.",
        default="DATASET",
        metavar="DATASET",
    )

    parser.add_argument(
        "-rows",
        "--rows-to-skip",
        type=int,
        help="Rows that should be skipped",
        default=1,
        metavar=1,
    )
    arguments = parser.parse_args()

    return arguments


def load_arguments():
    '''
    Load the arguments that the program will support.

    Returns
        - arguments (`argparse Object`): loaded arguments for the execution of the program.
    '''

    arguments = get_arguments()
    return arguments
