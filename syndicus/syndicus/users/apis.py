from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_spectacular.utils import extend_schema

from syndicus.api.pagination import (
    LimitOffsetPagination,
    get_paginated_response,
)
from .serializers import BaseUserSerializer
from .models import BaseUser
from .selectors import user_list


# TODO: When JWT is resolved, add authenticated version
class UserListApi(APIView):
    class Pagination(LimitOffsetPagination):
        default_limit = 1

    class FilterSerializer(serializers.Serializer):
        id = serializers.IntegerField(required=False)
        is_admin = serializers.BooleanField(required=False, allow_null=True, default=None)
        email = serializers.EmailField(required=False)

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = BaseUser
            fields = ("id", "email", "is_admin")

    @extend_schema(
        summary="List Users",
        description="Returns a list of users",
        responses={200: dict},
    )
    def get(self, request):
        # Make sure the filters are valid, if passed
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        users = user_list(filters=filters_serializer.validated_data)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.OutputSerializer,
            queryset=users,
            request=request,
            view=self,
        )

    def post(self, request):
        serializer = BaseUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailApi(APIView):
    # class OutputSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = BaseUser
    #         fields = ("id", "email", "is_admin")

    @extend_schema(
        summary="User Detail",
        description="Returns a specific users",
        responses={200: dict},
    )
    def get(self, request, id):
        try:
            building = BaseUser.objects.get(pk=pk)
            serializer = BaseUserSerializer(building)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except BaseUser.DoesNotExist:
            return Response(
                {"error": "Building not found"}, status=status.HTTP_404_NOT_FOUND
            )