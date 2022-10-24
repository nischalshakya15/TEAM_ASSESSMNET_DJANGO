import operator

import pandas as pd
from pandas.core.common import flatten

from api.constant.assessment_constant import *
from api.utils.df_utils import get_assessment_average, search_into_data_frame


def get_individual_average(data_frame):
    """
    For each row in the dataframe, get the average of the trust, conflict, commitment, result, and accountability
    columns

    :param data_frame: the data frame that you want to get the average for
    :return: A list of dictionaries.
    """
    individual_mean_list_of_dict = []

    for index, row in data_frame.iterrows():
        individual_mean_dict = {
            'Email Address': row['Email Address'],
            'Trust': get_assessment_average(row, TRUST_LIST),
            'Conflict': get_assessment_average(row, COMMITMENT_LIST),
            'Commitment': get_assessment_average(row, COMMITMENT_LIST),
            'Result': get_assessment_average(row, RESULT_LIST),
            'Accountability': get_assessment_average(row, RESULT_LIST)
        }
        individual_mean_list_of_dict.append(individual_mean_dict)

    return get_individual_average_data_frame(individual_mean_list_of_dict)


def get_individual_average_dict(data_frame):
    """
    For each row in the dataframe, get the average of the trust, conflict, commitment, result, and accountability
    columns

    :param data_frame: the data frame that you want to get the average for
    :return: A list of dictionaries.
    """
    individual_mean_list_of_dict = []

    for index, row in data_frame.iterrows():
        result_list_of_dict = [
            {'assessment': 'Trust', 'average': get_assessment_average(row, TRUST_LIST)},
            {'assessment': 'Conflict', 'average': get_assessment_average(row, CONFLICT_LIST)},
            {'assessment': 'Commitment', 'average': get_assessment_average(row, COMMITMENT_LIST)},
            {'assessment': 'Result', 'average': get_assessment_average(row, RESULT_LIST)},
            {'assessment': 'Accountability', 'average': get_assessment_average(row, ACCOUNTABILITY_LIST)}
        ]
        individual_mean_dict = {'email': row['Email Address'], 'result': result_list_of_dict}
        individual_mean_list_of_dict.append(individual_mean_dict)

    return individual_mean_list_of_dict


def get_individual_average_dict_by_column_name(data_frame, column_name, values):
    """
    It takes a dataframe, a column name, and a list of values, and returns a dictionary with the average of each assessment
    for the individual

    :param data_frame: the data frame that you want to search into
    :param column_name: The column name in the data frame that you want to search for
    :param values: the email address of the individual you want to get the average for
    :return: A list of dictionaries.
    """
    result_list_of_dict = []
    individual_df = search_into_data_frame(data_frame, column_name, values)

    for index, row in individual_df.iterrows():
        result_list_of_dict.append({'assessment': 'Trust', 'average': get_assessment_average(row, TRUST_LIST)})
        result_list_of_dict.append({'assessment': 'Conflict', 'average': get_assessment_average(row, CONFLICT_LIST)})
        result_list_of_dict.append(
            {'assessment': 'Commitment', 'average': get_assessment_average(row, COMMITMENT_LIST)})
        result_list_of_dict.append({'assessment': 'Result', 'average': get_assessment_average(row, RESULT_LIST)})
        result_list_of_dict.append(
            {'assessment': 'Accountability', 'average': get_assessment_average(row, ACCOUNTABILITY_LIST)})
        individual_mean_dict = {
            'email': row['Email Address'],
            'result': result_list_of_dict
        }
        return individual_mean_dict


def get_individual_average_data_frame(individual_mean_list_of_dict):
    """
    It takes a list of dictionaries, and returns a dataframe

    :param individual_mean_list_of_dict: a list of dictionaries, where each dictionary is the mean of the data for a
    single individual :return: A dataframe of the individual mean list of dict
    """
    return pd.DataFrame.from_dict(individual_mean_list_of_dict)


def get_individual_data_frame(data_frame, column_name, column_values):
    """
    It takes a data frame, a column name, and a list of values, and returns a data frame with the average of the values in
    the list of values

    :param data_frame: The data frame that you want to search into
    :param column_name: The name of the column you want to search in
    :param column_values: The values of the column you want to search for
    :return: A data frame with the average of each assessment for a given student.
    """
    individual_data = search_into_data_frame(data_frame, column_name, column_values).replace(ASSESSMENT_DICT)
    trust = individual_data[TRUST_LIST]
    conflict = individual_data[CONFLICT_LIST]
    commitment = individual_data[COMMITMENT_LIST]
    results = individual_data[RESULT_LIST]
    accountability = individual_data[ACCOUNTABILITY_LIST]
    assessment_list = [trust.columns.tolist(), conflict.columns.tolist(), commitment.columns.tolist(),
                       results.columns.tolist(), accountability.columns.tolist()]
    assessment_value = [trust.values[0], conflict.values[0], commitment.values[0], results.values[0],
                        accountability.values[0]]
    return pd.DataFrame.from_dict(
        {'Assessment': list(flatten(assessment_list)), 'Value': list(flatten(assessment_value))})


def get_individual_dict(data_frame, column_name, column_values):
    """
    It takes in a dataframe, a column name, and a list of values to search for in that column. It then returns a list of
    dictionaries, each dictionary containing the email, the assessment type, and the assessment result

    :param data_frame: The data frame that you want to search into
    :param column_name: The column name in the dataframe that you want to search for
    :param column_values: This is the email address of the person you want to get the data for
    :return: A list of dictionaries.
    """
    individual_data = search_into_data_frame(data_frame, column_name, column_values).replace(ASSESSMENT_DICT)
    trust = individual_data[TRUST_LIST]
    conflict = individual_data[CONFLICT_LIST]
    commitment = individual_data[COMMITMENT_LIST]
    results = individual_data[RESULT_LIST]
    accountability = individual_data[ACCOUNTABILITY_LIST]
    assessment_list = [trust.columns.tolist(), conflict.columns.tolist(), commitment.columns.tolist(),
                       results.columns.tolist(), accountability.columns.tolist()]
    assessment_value = [trust.values[0], conflict.values[0], commitment.values[0], results.values[0],
                        accountability.values[0]]

    trust_dict = []
    conflict_dict = []
    commitment_dict = []
    result_dict = []
    accountability_dict = []

    header = list(flatten(assessment_list))
    mean_value = list(flatten(assessment_value))

    for i in range(0, 8):
        trust_dict.append({"assessment": header[i], "average": mean_value[i]})

    for i in range(8, 16):
        conflict_dict.append({"assessment": header[i], "average": mean_value[i]})

    for i in range(16, 23):
        commitment_dict.append({"assessment": header[i], "average": mean_value[i]})

    for i in range(23, 31):
        result_dict.append({"assessment": header[i], "average": mean_value[i]})

    for i in range(31, len(mean_value)):
        accountability_dict.append({"assessment": header[i], "average": mean_value[i]})

    return [
        {
            "email": column_values[0],
            "assessment_result": [
                {"assessment_type": "Trust", "result": trust_dict},
                {"assessment_type": "Conflict", "result": conflict_dict},
                {"assessment_type": "Commitment", "result": commitment_dict},
                {"assessment_type": "Result", "result": result_dict},
                {"assessment_type": "Accountability", "result": accountability_dict}
            ]
        }
    ]


def get_individual_dict_sorted(data_frame, column_name, column_values, is_sort):
    """
    This function takes in a dataframe, a column name, a list of column values, and a boolean value. It returns a list of
    dictionaries, where each dictionary contains the name of an assessment and the average score for that assessment

    :param data_frame: The data frame that you want to search into
    :param column_name: The column name in the data frame that you want to search for
    :param column_values: This is the value of the column you want to search for
    :param is_sort: True or False. If True, the results will be sorted by average
    :return: A list of dictionaries.
    """
    individual_data = search_into_data_frame(data_frame, column_name, column_values).replace(ASSESSMENT_DICT)
    trust = individual_data[TRUST_LIST]
    conflict = individual_data[CONFLICT_LIST]
    commitment = individual_data[COMMITMENT_LIST]
    results = individual_data[RESULT_LIST]
    accountability = individual_data[ACCOUNTABILITY_LIST]
    assessment_list = [trust.columns.tolist(), conflict.columns.tolist(), commitment.columns.tolist(),
                       results.columns.tolist(), accountability.columns.tolist()]
    assessment_value = [trust.values[0], conflict.values[0], commitment.values[0], results.values[0],
                        accountability.values[0]]

    result_dict = []

    header = list(flatten(assessment_list))
    mean_value = list(flatten(assessment_value))

    for i in range(0, len(header)):
        result_dict.append({"assessment": header[i], "average": mean_value[i]})

    if is_sort == 'True':
        result_dict.sort(key=operator.itemgetter('average'))

    return result_dict


def get_all_individual_dict(data_frame):
    """
    It takes in a dataframe, and returns a list of dictionaries, where each dictionary contains the email address of the
    individual, and the assessment results for each of the 5 assessment types

    :param data_frame: The data frame that you want to search into
    :return: A list of dictionaries.
    """
    emails = data_frame['Email Address']
    response = []
    for email in emails:
        email = [email]
        individual_data = search_into_data_frame(data_frame, 'Email Address', email).replace(ASSESSMENT_DICT)
        trust = individual_data[TRUST_LIST]
        conflict = individual_data[CONFLICT_LIST]
        commitment = individual_data[COMMITMENT_LIST]
        results = individual_data[RESULT_LIST]
        accountability = individual_data[ACCOUNTABILITY_LIST]
        assessment_list = [trust.columns.tolist(), conflict.columns.tolist(), commitment.columns.tolist(),
                           results.columns.tolist(), accountability.columns.tolist()]
        assessment_value = [trust.values[0], conflict.values[0], commitment.values[0], results.values[0],
                            accountability.values[0]]

        trust_dict = []
        conflict_dict = []
        commitment_dict = []
        result_dict = []
        accountability_dict = []

        header = list(flatten(assessment_list))
        mean_value = list(flatten(assessment_value))

        for i in range(0, 8):
            trust_dict.append({"assessment": header[i], "average": mean_value[i]})

        for i in range(8, 16):
            conflict_dict.append({"assessment": header[i], "average": mean_value[i]})

        for i in range(16, 23):
            commitment_dict.append({"assessment": header[i], "average": mean_value[i]})

        for i in range(23, 31):
            result_dict.append({"assessment": header[i], "average": mean_value[i]})

        for i in range(31, len(mean_value)):
            accountability_dict.append({"assessment": header[i], "average": mean_value[i]})

        response.append(
            {
                "email": email[0],
                "assessment_result": [
                    {"assessment_type": "Trust", "result": trust_dict},
                    {"assessment_type": "Conflict", "result": conflict_dict},
                    {"assessment_type": "Commitment", "result": commitment_dict},
                    {"assessment_type": "Result", "result": result_dict},
                    {"assessment_type": "Accountability", "result": accountability_dict}
                ]
            }
        )

    return response
