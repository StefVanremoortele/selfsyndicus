from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Building, Privative
from .serializers import BuildingSerializer, PrivativeSerializer
from drf_spectacular.utils import extend_schema

class BuildingAPIView(APIView):
    @extend_schema(
        summary="List Buildings",
        description="Returns a list of buildings",
        responses={200: dict},
    )
    def get(self, request, pk=None):
        if pk:
            try:
                building = Building.objects.get(pk=pk)
                serializer = BuildingSerializer(building)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Building.DoesNotExist:
                return Response(
                    {"error": "Building not found"}, status=status.HTTP_404_NOT_FOUND
                )
        else:
            buildings = Building.objects.all()
            serializer = BuildingSerializer(buildings, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Create Building",
        description="Creates a new building",
        responses={200: dict},
        request=BuildingSerializer,
    )
    def post(self, request):
        serializer = BuildingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            building = Building.objects.get(pk=pk)
        except Building.DoesNotExist:
            return Response(
                {"error": "Building not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = BuildingSerializer(building, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            building = Building.objects.get(pk=pk)
            building.delete()
            return Response(
                {"message": "Building deleted successfully"},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Building.DoesNotExist:
            return Response(
                {"error": "Building not found"}, status=status.HTTP_404_NOT_FOUND
            )

class PrivativeAPIView(APIView):
    @extend_schema(
        summary="List Privatives",
        description="Returns a list of privatives",
        responses={200: dict},
    )
    def get(self, request, building_id=None):
        if building_id:
            privatives = Privative.objects.filter(building_id=building_id)
        else:
            privatives = Privative.objects.all()

        serializer = PrivativeSerializer(privatives, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # if pk:
        #     try:
        #         privative = Privative.objects.get(pk=pk)
        #         serializer = BuildingSerializer(privative)
        #         return Response(serializer.data, status=status.HTTP_200_OK)
        #     except Building.DoesNotExist:
        #         return Response(
        #             {"error": "Privative not found"}, status=status.HTTP_404_NOT_FOUND
        #         )
        # else:
        #     # if building_id:
        #     #     privatives = Privative.objects.get(building_id=building_id)
        #     #     serializer = PrivativeSerializer(privatives, many=True)
        #     #     return Response(serializer.data, status=status.HTTP_200_OK)
        #     privatives = Privative.objects.all()
        #     serializer = PrivativeSerializer(privatives, many=True)
        #     return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Create Privative",
        description="Creates a new privative",
        responses={200: dict},
        request=PrivativeSerializer,
    )
    def post(self, request, building_id=None):
        serializer = PrivativeSerializer(data=request.data)
        if serializer.is_valid():
            if building_id:
                serializer.validated_data['building'] = building_id  # Associate with the building if provided
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
            return Response(serializer.data, status=status.HTTP_200_OK)
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
