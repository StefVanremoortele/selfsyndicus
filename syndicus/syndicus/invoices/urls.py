from django.urls import path, include

urlpatterns = [
    path("", InvoiceListAPIView.as_view(), name="invoice-list"),
    path("<int:pk>/", InvoiceDetailAPIView.as_view(), name="invoice-detail"),
]