from django.urls import path, include

# from rest_framework.routers import DefaultRouter
from .apis import (
    PrivativeDetailAPIView,
    PrivativesListAPIView,
    #     BuildingDetailAPIView,
    #     PrivativeDetailAPIView,
    #     PrivativeDetailByBuildingAPIView,
    #     PrivativeListAPIView,
    #     PrivativeListByBuildingAPIView,
)


urlpatterns = [
    path("", PrivativesListAPIView.as_view(), name="privatives-list"),
    path("<int:pk>/", PrivativeDetailAPIView.as_view(), name="privative-detail"),
]
