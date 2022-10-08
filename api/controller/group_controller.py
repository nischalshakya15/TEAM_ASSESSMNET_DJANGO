from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from api.dao.assessment_dao import read_assessment_data_from_csv
from api.service.group.group_assessment_service import get_group_average_dict, get_group_average, \
    get_sorted_average_of_average, get_group_average_sorted_dict


# This class is a subclass of the APIView class, and it's purpose is to return the average of a group of numbers.
class GroupAverage(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request):
        """
        It takes a csv file, reads it, and returns a dictionary of the average scores for each group

        :param request: The request object is a standard Django request object. It contains all the information about the
        request that was made to the server
        :return: The group_mean_sorted is being returned.
        """
        df = read_assessment_data_from_csv(request.FILES['file'])
        is_group_by_assessment = request.GET.get('group-by-assessment')
        is_sort = request.GET.get('sorted')
        if is_group_by_assessment == 'False' and is_sort:
            return Response(get_group_average_sorted_dict(df, is_sort), status=HTTP_200_OK)

        group_average = get_group_average_dict(df)
        return Response(group_average, status=HTTP_200_OK)


# This class is a subclass of the APIView class, and it's purpose is to return the average of the average of the group's
# scores.
class GroupAverageOfAverage(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request):
        """
        It takes a csv file, reads it, calculates the average of each group, sorts the averages, and returns the sorted
        averages

        :param request: The request object is a standard Django request object. It contains all the information about the
        request that was made to the server
        :return: The average of the average of the group.
        """
        df = read_assessment_data_from_csv(request.FILES['file'])
        group_mean = get_group_average(df, False)
        group_mean_sorted = get_sorted_average_of_average(group_mean)
        return Response(group_mean_sorted, status=HTTP_200_OK)
