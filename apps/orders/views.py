from rest_framework import generics, permissions
from .models import Order
from .serializers import OrderSerializer
from rest_framework.pagination import PageNumberPagination

class OrderPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
    max_page_size = 100

class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = OrderPagination
