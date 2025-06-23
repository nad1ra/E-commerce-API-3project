from django.urls import path
from .views import UserProfileView

app_name = "profile"

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]
