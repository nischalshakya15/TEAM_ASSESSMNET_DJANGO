from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from api.dao.assessment_dao import read_assessment_data_from_csv
from api.service.individual.individual_assessment_service import *


# This class is a subclass of the APIView class, which is a subclass of the View class
class IndividualAssessment(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request):
        """
        It takes a CSV file, reads it, and returns a JSON response with the data

        :param request: The request object is a standard Django request object
        :return: The function get_all_individual_dict() returns a dictionary of all the individuals in the dataframe.
        """
        df = read_assessment_data_from_csv(request.FILES['file'])
        email = request.GET.get('email')
        is_group_by_assessment = request.GET.get('group-by-assessment')
        is_sort = request.GET.get('sorted')

        if email and not is_group_by_assessment and not is_sort:
            return Response(get_individual_dict(df, 'Email Address', [email]),
                            status=HTTP_200_OK)

        if email and is_group_by_assessment == 'False' and is_sort:
            return Response(get_individual_dict_sorted(df, 'Email Address', [email], is_sort),
                            status=HTTP_200_OK)

        return Response(get_all_individual_dict(df),
                        status=HTTP_200_OK)


# This class is a subclass of the APIView class, and it's purpose is to return the average of a specific individual's
# ratings.
class IndividualAverage(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request):
        """
        It takes a CSV file, reads it, and returns a dictionary of the average scores for each individual

        :param request: The request object is a standard Django request object
        :return: The average score for each individual.
        """
        df = read_assessment_data_from_csv(request.FILES['file'])
        email = request.GET.get('email')
        if email:
            return Response(get_individual_average_dict_by_column_name(df, 'Email Address', [email]),
                            status=HTTP_200_OK)
        else:
            return Response(get_individual_average_dict(df), status=HTTP_200_OK)
