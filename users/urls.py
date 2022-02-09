from django.urls import path

from .views import UserFollowsView

app_name = "users"


urlpatterns = [
    path('', UserFollowsView.as_view(), name="follows"),
]
