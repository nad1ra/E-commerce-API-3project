from django.urls import path
from .views import (
    ProductListCreateView, ProductDetailView,
    LikeCreateView
)

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/<int:pk>/like/', LikeCreateView.as_view(), name='like-create'),
]
