from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import 
from drf_spectacular.utils import extend_schema

class InvoiceListAPIView(APIView):
    serializer_class = InvoiceSerializer

    @extend_schema(
        operation_id="invoice_list",
        summary="List Invoices",
        description="Returns a list of invoices",
        responses={200: dict},
    )
    def get(self, request):
        buildings = Invoice.objects.all()
        serializer = InvoiceSerializer(buildings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)