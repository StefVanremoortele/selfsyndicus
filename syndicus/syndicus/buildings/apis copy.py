from rest_framework import serializers
from rest_framework.views import APIView

from drf_spectacular.utils import extend_schema

from syndicus.syndicus.api.pagination import LimitOffsetPagination, get_paginated_response

# TODO: When JWT is resolved, add authenticated version
class BuildingListApi(APIView):
    class Pagination(LimitOffsetPagination):
        default_limit = 1

    class FilterSerializer(serializers.Serializer):
        id = serializers.IntegerField(required=False)
        is_admin = serializers.BooleanField(required=False, allow_null=True, default=None)
        email = serializers.EmailField(required=False)

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Building
            fields = ("id", "email", "is_admin")

    # @extend_schema(
    #     summary="List Buildings",
    #     description="Returns a list of buildings",
    #     responses={200: dict},
    # )
    def get(self, request):
        # Make sure the filters are valid, if passed
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        buildings = building_list(filters=filters_serializer.validated_data)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.OutputSerializer,
            queryset=building,
            request=request,
            view=self,
        )