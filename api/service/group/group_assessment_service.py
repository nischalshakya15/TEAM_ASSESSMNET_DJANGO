import operator

import pandas as pd

from api.constant.assessment_constant import *
from api.utils.df_utils import get_assessment_average, search_into_data_frame


def get_group_average(data_frame, is_sort_by_average):
    """
    For each group, get the average of each assessment type

    :param is_sort_by_average: boolean value that indicate whether to sort by average or not
    :param data_frame: the dataframe you want to get the average of
    :return: A dataframe with the average of each question for each group.
    """
    group_average = pd.concat([
        get_assessment_average(data_frame, TRUST_LIST),
        get_assessment_average(data_frame, CONFLICT_LIST),
        get_assessment_average(data_frame, COMMITMENT_LIST),
        get_assessment_average(data_frame, RESULT_LIST),
        get_assessment_average(data_frame, ACCOUNTABILITY_LIST)
    ], axis=0)

    return get_group_average_data_frame(group_average, is_sort_by_average)


def get_group_average_dict(data_frame):
    """
    It takes a dataframe as input, and returns a list of dictionaries, where each dictionary contains the average score for
    each assessment type

    :param data_frame: the dataframe that contains the data
    :return: A list of dictionaries.
    """
    group_average = pd.concat([
        get_assessment_average(data_frame, TRUST_LIST),
        get_assessment_average(data_frame, CONFLICT_LIST),
        get_assessment_average(data_frame, COMMITMENT_LIST),
        get_assessment_average(data_frame, RESULT_LIST),
        get_assessment_average(data_frame, ACCOUNTABILITY_LIST)
    ], axis=0)

    header = group_average.index.tolist()
    mean_value = group_average.values.tolist()

    trust_dict = []
    conflict_dict = []
    commitment_dict = []
    result_dict = []
    accountability_dict = []

    for i in range(0, 8):
        trust_dict.append({"assessment": header[i], "average": mean_value[i]})

    for i in range(8, 16):
        conflict_dict.append({"assessment": header[i], "average": mean_value[i]})

    for i in range(16, 23):
        commitment_dict.append({"assessment": header[i], "average": mean_value[i]})

    for i in range(23, 31):
        result_dict.append({"assessment": header[i], "average": mean_value[i]})

    for i in range(31, len(group_average)):
        accountability_dict.append({"assessment": header[i], "average": mean_value[i]})

    return [
        {"assessment_type": "Trust", "result": trust_dict},
        {"assessment_type": "Conflict", "result": conflict_dict},
        {"assessment_type": "Commitment", "result": commitment_dict},
        {"assessment_type": "Result", "result": result_dict},
        {"assessment_type": "Accountability", "result": accountability_dict}
    ]


def get_group_average_sorted_dict(data_frame, is_sort):
    """
    It takes a dataframe as input, and returns a list of dictionaries, where each dictionary contains the average score for
    each assessment type

    :param data_frame: the dataframe that contains the data
    :return: A list of dictionaries.
    """
    group_average = pd.concat([
        get_assessment_average(data_frame, TRUST_LIST),
        get_assessment_average(data_frame, CONFLICT_LIST),
        get_assessment_average(data_frame, COMMITMENT_LIST),
        get_assessment_average(data_frame, RESULT_LIST),
        get_assessment_average(data_frame, ACCOUNTABILITY_LIST)
    ], axis=0)

    header = group_average.index.tolist()
    mean_value = group_average.values.tolist()

    result_dict = []

    for i in range(0, len(header)):
        result_dict.append({"assessment": header[i], "average": mean_value[i]})

    if is_sort == 'True':
        result_dict.sort(key=operator.itemgetter('average'))

    return result_dict


def get_group_average_data_frame(group_average, is_sort_by_average):
    """
    It takes a pandas series, converts it to a list, and then converts it to a dataframe.

    :param is_sort_by_average: boolean value that indicate whether to sort by average or not
    :param group_average: a pandas series with the average of each assessment for each group
    :return: A dataframe with the average of each assessment for each group.
    """
    header = group_average.index.tolist()
    mean_value = group_average.values.tolist()
    if is_sort_by_average:
        return pd.DataFrame.from_dict({ASSESSMENT: header, AVERAGE: mean_value}).sort_values(
            by=[AVERAGE])
    else:
        return pd.DataFrame.from_dict({ASSESSMENT: header, AVERAGE: mean_value})


def get_sorted_average_of_average(group_mean_data_frame):
    """
    It takes in a dataframe, searches for the columns that are in the lists above, and then calculates the mean of those
    columns.
    :param group_mean_data_frame: This is the data frame that contains the average of each group
    :return: A dictionary with the sorted average of the average of the group.
    """
    trust_avg = search_into_data_frame(group_mean_data_frame,
                                       ASSESSMENT, TRUST_LIST).mean(axis=0, numeric_only=True)
    conflict_avg = search_into_data_frame(group_mean_data_frame,
                                          ASSESSMENT, CONFLICT_LIST).mean(axis=0, numeric_only=True)
    commitment_avg = search_into_data_frame(group_mean_data_frame,
                                            ASSESSMENT, COMMITMENT_LIST).mean(axis=0, numeric_only=True)
    result_avg = search_into_data_frame(group_mean_data_frame,
                                        ASSESSMENT, RESULT_LIST).mean(axis=0, numeric_only=True)
    accountability_avg = search_into_data_frame(group_mean_data_frame,
                                                ASSESSMENT, ACCOUNTABILITY_LIST).mean(axis=0, numeric_only=True)

    data = [
        round(float(trust_avg), ROUND_DECIMAL), round(float(conflict_avg), ROUND_DECIMAL),
        round(float(commitment_avg), ROUND_DECIMAL), round(float(result_avg), ROUND_DECIMAL),
        round(float(accountability_avg), ROUND_DECIMAL)
    ]
    data_map = {'Trust': data[0], 'Conflict': data[1], 'Commitment': data[2], 'Result': data[3],
                'Accountability': data[4]}
    sorted_data_map = {k: v for k, v in sorted(data_map.items(), key=lambda item: item[1])}
    sorted_data = []
    for key in sorted_data_map:
        sorted_data.append({'assessment': key, 'average': sorted_data_map[key]})

    return sorted_data
