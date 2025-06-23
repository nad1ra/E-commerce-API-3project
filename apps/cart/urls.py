from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.CartListCreateView.as_view(), name='list-create'),
    path('cart/delete/', views.CartDeleteView.as_view(), name='cart-delete')
]
