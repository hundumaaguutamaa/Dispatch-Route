from django.shortcuts import render

from rest_framework import viewsets, filters
from .models import ITTeam, ContactPerson, ITRequest
from .serializers import ITTeamSerializer, ContactPersonSerializer, ITRequestSerializer
from django_filters.rest_framework import DjangoFilterBackend

# ViewSet for ITTeam
class ITTeamViewSet(viewsets.ModelViewSet):
    queryset = ITTeam.objects.all()  # Query all IT teams from the database
    serializer_class = ITTeamSerializer  # Use the ITTeamSerializer for data transformation
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]  # Enable filtering and search functionality
    filterset_fields = ['name']  # Allow filtering by team name
    search_fields = ['name']  # Enable search by team name

# ViewSet for ContactPerson
class ContactPersonViewSet(viewsets.ModelViewSet):
    queryset = ContactPerson.objects.all()  # Query all contact persons
    serializer_class = ContactPersonSerializer  # Use the ContactPersonSerializer for data transformation
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]  # Enable filtering and search functionality
    filterset_fields = ['team__name']  # Allow filtering by team name (related field)
    search_fields = ['name', 'email']  # Enable search by name or email

# ViewSet for ITRequest
class ITRequestViewSet(viewsets.ModelViewSet):
    queryset = ITRequest.objects.all()  # Query all IT requests
    serializer_class = ITRequestSerializer  # Use the ITRequestSerializer for data transformation
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]  # Enable filtering and search functionality
    filterset_fields = ['team__name']  # Allow filtering by team name and status
    search_fields = ['title', 'description']  # Enable search by title or description of the request

