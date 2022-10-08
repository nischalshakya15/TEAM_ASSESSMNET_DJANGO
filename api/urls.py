from django.urls import path

from .controller.email_controller import Emails
from .controller.group_controller import GroupAverage, GroupAverageOfAverage
from .controller.individual_controller import IndividualAssessment, IndividualAverage

urlpatterns = [
    path('assessment/group/average', GroupAverage.as_view()),
    path('assessment/group/average-of-average', GroupAverageOfAverage.as_view()),
    path('assessment/individual/emails', Emails.as_view()),
    path('assessment/individual', IndividualAssessment.as_view()),
    path('assessment/individual/average', IndividualAverage.as_view()),
]
