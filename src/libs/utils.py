'''
    Spreedsheet and Data Files Helper
'''
# standard
import os
import logging
import json
import pandas
import re

# third party


# local
from libs import constants as EC


def get_data_frame(filename: str, load_sheet, rows_to_skip: int) -> pandas.DataFrame:
    '''
    Read and convert the Excel file to Panda DataFrame.

    Param
        - filename (`String`): full XLSX file path.
        - load_sheet (`Integer`): Excel sheet number that will be loaded.
        - rows_to_skip (`Integer`): number of rows to skip.

    Returns
        - dataset_df (`pandas.DataFrame`): DataFrame with the Datasets Record Excel file data.
    '''
    dataset_df = pandas.read_excel(
        filename, sheet_name=load_sheet, skiprows=rows_to_skip)
    return dataset_df


def get_author_data_frame(filename: str, load_sheet, rows_to_skip: int) -> pandas.DataFrame:
    '''
    Read and convert the Excel file to Panda DataFrame.

    Param
        - filename (`String`): full XLSX file path.
        - load_sheet (`Integer`): Excel sheet number that will be loaded.
        - rows_to_skip (`Integer`): number of rows to skip.

    Returns
        - dataset_df (`pandas.DataFrame`): DataFrame with the Datasets Record Excel file data.
    '''
    dataset_df = pandas.read_excel(
        filename, sheet_name=load_sheet, skiprows=rows_to_skip, index_col=0)
    nan_value = float("NaN")
    dataset_df.replace("", nan_value, inplace=True)
    dataset_df.dropna(how='all', axis=1, inplace=True)
    return dataset_df


def get_data_frame_tsv(filename: str) -> pandas.DataFrame:
    '''
    Read and convert the TSV/CSV file to Panda DataFrame.

    Param
        - filename (`String`): full TSV/CSV file path.

    Returns
        - dataset_df (`pandas.DataFrame`): DataFrame with the Datasets Record Excel file data.
    '''
    dataset_df = pandas.read_csv(filename, sep='\t', header=0, index_col=False)
    return dataset_df


def get_json_from_data_frame(data_frame: pandas.DataFrame) -> dict:
    '''
    Converts DataFrame into JSON format.

    Param
        - data_frame (`pandas.DataFrame`): DataFrame with the Datasets Record Excel file data.

    Returns
        - json_dict (`Dict`): JSON string converted  to a dictionary.
    '''
    string_json = data_frame.to_json(orient='records')
    string_json = re.sub(r'\([0-9]\)\s*', '', string_json)
    json_dict = json.loads(string_json)
    return json_dict


def get_excel_data(filename: str, load_sheet, rows_to_skip: int) -> dict:
    '''
    Process the XLSX file as a DataFrame and return it as a JSON object

    Param
        - filename (`String`): Excel file name.

    Returns
        - data_frame_json (`Dict`): json dictionary with the Excel data.
    '''
    data_frame = get_data_frame(filename, load_sheet, rows_to_skip)
    data_frame_json = get_json_from_data_frame(data_frame)
    return data_frame_json


def get_tsv_data(filename: str) -> dict:
    '''
    Process the TSV/CSV file as a DataFrame and return it as a JSON object

    Param
        - filename (`String`): TSV/CSV file name.

    Returns
        - data_frame_json (`Dict`): json dictionary with the TSV/CSV data.
    '''
    data_frame = get_data_frame_tsv(filename)
    data_frame_json = get_json_from_data_frame(data_frame)
    return data_frame_json


def validate_directories(data_path):
    '''
    Verify if the output path directories exists.

    Param
        - data_path (String): directories path.

    Raises
        - (IOError): If not valid directory
    '''
    if not os.path.isdir(data_path):
        raise IOError(f'Please, verify \'{data_path}\' directory path')


def validate_excel_file(excel_path):
    '''
    This function filters the XLSX file from the directory path.

    Param
        - excel_path (`String`): excel file path.

    Raises
        - (IOError): If not valid excel file.
    '''
    if not os.path.isfile(excel_path) and excel_path.endswith('.xlsx'):
        raise IOError(
            f'\'{excel_path}\' is not a valid XLSX file will be ignored')
