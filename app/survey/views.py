from rest_framework import viewsets
from .models import SurveyForm
from .serializers import SurveyFormSerializer

class SurveyFormViewSet(viewsets.ModelViewSet):
    queryset = SurveyForm.objects.all()
    serializer_class = SurveyFormSerializer
