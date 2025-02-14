from rest_framework import serializers
from .models import SurveyForm

class SurveyFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyForm
        fields = '__all__'
