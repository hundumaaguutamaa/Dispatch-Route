from django.urls import path
from .views import TeamCreateView, RequestCreateView, search, TeamListView

urlpatterns = [
    path('teams/', TeamListView.as_view(), name='list_teams'),  # Endpoint for listing teams
    path('teams/create/', TeamCreateView.as_view(), name='add_team'),  # Endpoint for creating a team
    path('requests/', RequestCreateView.as_view(), name='add_request'),  # Endpoint for creating a request
    path('search/', search, name='search'),  # Endpoint for searching
]
