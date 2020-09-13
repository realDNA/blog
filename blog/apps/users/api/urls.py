from django.urls import path
from apps.users.api.views import CurrentUserAPIView

app_name = 'users-api'

urlpatterns = [
    path("user/", CurrentUserAPIView.as_view(), name="current-user")
]
