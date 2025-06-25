from django.urls import path
from profiles.views import UserProfileView

app_name = 'profiles'

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]

