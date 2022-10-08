from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from api.dao.assessment_dao import read_assessment_data_from_csv


# This class is a subclass of the APIView class, which is a subclass of the View class
class Emails(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request):
        """
        It takes a file from the request, reads it into a dataframe, and returns the email addresses from the dataframe

        :param request: The request object is a HttpRequest object. It contains all the information about the request sent
        by the client
        :return: The email address of the user.
        """
        df = read_assessment_data_from_csv(request.FILES['file'])
        return Response(df['Email Address'], status=HTTP_200_OK)
