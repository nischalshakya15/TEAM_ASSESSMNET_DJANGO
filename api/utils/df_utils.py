from api.constant.assessment_constant import ASSESSMENT_DICT, ROUND_DECIMAL


def get_assessment_average(data_frame, assessment_list):
    """
    Get the mean of the assessment_list
    :param data_frame: dataframe
    :param assessment_list: List of assessment types
    :return: Mean value
    """
    mean = data_frame[assessment_list].replace(ASSESSMENT_DICT).mean(axis=0)
    return round(mean, ROUND_DECIMAL)


def export_to_csv(data_frame, file_name):
    """
    This function takes a data frame and a file name as input, and exports the data frame to a csv file with the given
    file name

    :param data_frame: The data frame you want to export to a CSV file
    :param file_name: The name of the file you want to export to
    """
    data_frame.to_csv(file_name, index=False)


def search_into_data_frame(data_frame, column_name, column_values):
    """
    It takes a data frame, a column name, and a list of values, and returns a data frame containing only the rows that have
    the specified values in the specified column

    :param data_frame: The data frame you want to search into
    :param column_name: The name of the column you want to search in
    :param column_values: The values you want to search for in the column
    :return: A dataframe with the rows that have the column_values in the column_name column.
    """
    return data_frame.loc[data_frame[column_name].isin(column_values)]


def get_columns_from_data_frame(data_frame):
    """
    This function takes a data frame as input and returns a list of the column names

    :param data_frame: The data frame that you want to get the columns from
    :return: A list of the column names in the data frame.
    """
    return data_frame.columns.tolist()


def get_rows_from_data_frame(data_frame):
    """
    "Get the rows from the data frame."

    The function takes a data frame as input and returns a list of lists

    :param data_frame: The data frame to get the rows from
    :return: A list of lists.
    """
    return data_frame.values.tolist()
