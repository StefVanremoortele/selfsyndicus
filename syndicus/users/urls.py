from django.urls import path

from .apis import UserDetailApi, UserListApi

urlpatterns = [
    path("", UserListApi.as_view(), name="list"),
    path("<int:pk>/", UserDetailApi.as_view(), name="user-detail"),
]
