from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SurveyFormViewSet

router = DefaultRouter()
router.register(r'surveys', SurveyFormViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
