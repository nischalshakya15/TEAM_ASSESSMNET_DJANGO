import pandas as pd


def read_assessment_data_from_csv(file_name):
    """
       Read the data from the csv file
       :return:
       """
    return pd.read_csv(file_name)
