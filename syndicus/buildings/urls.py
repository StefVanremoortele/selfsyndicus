# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import BuildingViewSet

# router = DefaultRouter()
# router.register(r'buildings', BuildingViewSet, basename='building')

# urlpatterns = [
#     path('api/', include(router.urls)),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .apis import (
    BuildingListAPIView,
    BuildingDetailAPIView,
    # PrivativeDetailAPIView,
    # PrivativeDetailByBuildingAPIView,
    # PrivativeListAPIView,
    # PrivativeListByBuildingAPIView,
)


urlpatterns = [
    path("", BuildingListAPIView.as_view(), name="building-list"),
    path("<int:pk>/", BuildingDetailAPIView.as_view(), name="building-detail"),
    # path("privatives/", PrivativeListAPIView.as_view(), name="privative-list"),
    # path(
    #     "privatives/<int:pk>", PrivativeDetailAPIView.as_view(), name="privative-detail"
    # ),
    # path(
    #     "<int:building_id>/privatives/",
    #     PrivativeListByBuildingAPIView.as_view(),
    #     name="privative-list-by-building",
    # ),
    # path(
    #     "<int:building_id>/privatives/<int:privative_id>/",
    #     PrivativeDetailByBuildingAPIView.as_view(),
    #     name="privative-detail-by-building",
    # )
]
