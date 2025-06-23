from django.urls import path
from .views import ReviewCreateView

urlpatterns = [
    path('products/<int:pk>/review/', ReviewCreateView.as_view(), name='product-review-create'),
]
