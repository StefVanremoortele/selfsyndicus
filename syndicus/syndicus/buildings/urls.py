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
from .apis import BuildingAPIView, PrivativeAPIView


urlpatterns = [
    path("api/buildings/", BuildingAPIView.as_view(), name="building-list-create"),
    path("api/buildings/<int:pk>/", BuildingAPIView.as_view(), name="building-detail"),
    # path(
    #     "api/buildings/<int:pk>/privatives",
    #     PrivativeAPIView.as_view(),
    #     name="privative-list",
    # ),
        path('api/privatives/', PrivativeAPIView.as_view(), name='privative-list-create'),
        path('api/buildings/<int:building_id>/privatives/', PrivativeAPIView.as_view(), name='privative-list-by-building'),
    # path(
    #     "api/buildings/<int:pk>/privatives/<int:pk>",
    #     PrivativeAPIView.as_view(),
    #     name="privative-detail",
    # ),
]
