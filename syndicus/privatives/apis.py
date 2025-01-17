from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema

from .models import Privative
from .serializers import PrivativeSerializer


class PrivativesListAPIView(APIView):
    serializer_class = PrivativeSerializer

    @extend_schema(
        operation_id="privative_list",
        summary="List Privatives",
        description="Returns a list of privatives",
        responses={200: dict},
    )
    def get(self, request):
        privatives = Privative.objects.all()
        serializer = PrivativeSerializer(privatives, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        operation_id="privative_create",
        summary="Create Privative",
        description="Creates a new privative",
        responses={200: dict},
        request=PrivativeSerializer,
    )
    def post(self, request):
        serializer = PrivativeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PrivativeDetailAPIView(APIView):
    serializer_class = PrivativeSerializer

    @extend_schema(
        operation_id="privative_retrieve",
        summary="List Privatives",
        description="Returns a list of privatives",
        responses={200: dict},
    )
    def get(self, request, pk):
        if pk:
            try:
                privative = Privative.objects.get(pk=pk)
                serializer = PrivativeSerializer(privative)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Privative.DoesNotExist:
                return Response(
                    {"error": "Privative not found"}, status=status.HTTP_404_NOT_FOUND
                )
        else:
            privatives = Privative.objects.all()
            serializer = PrivativeSerializer(privatives, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            privative = Privative.objects.get(pk=pk)
        except Privative.DoesNotExist:
            return Response(
                {"error": "Privative not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = PrivativeSerializer(privative, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            privative = Privative.objects.get(pk=pk)
            privative.delete()
            return Response(
                {"message": "Privative deleted successfully"},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Privative.DoesNotExist:
            return Response(
                {"error": "Privative not found"}, status=status.HTTP_404_NOT_FOUND
            )