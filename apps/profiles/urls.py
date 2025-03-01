from django.urls import path
from apps.profiles.views import (
    AgentListApiView,
    GetProfileApiView,
    TopAgentListApiView,
    UpdateProfileApiView,
)

urlpatterns = [
    path("me/", GetProfileApiView.as_view(), name="get_profile"),
    path(
        "update/<str:username>/", UpdateProfileApiView.as_view(), name="update_profile"
    ),
    path("agents/all/", AgentListApiView.as_view(), name="all_agents"),
    path("top-agents/all/", TopAgentListApiView.as_view(), name="top_agents"),
]
