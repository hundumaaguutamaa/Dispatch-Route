from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import ITTeam, ContactPerson, ITRequest
from .serializers import ITTeamSerializer, ContactPersonSerializer, ITRequestSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse
from django.db.models import Q
from .models import ITTeam, ITRequest, ContactPerson

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

def search(request):
    query = request.GET.get('q', '')
    if query:
        # Search for ITTeams by name
        teams = ITTeam.objects.filter(name__icontains=query)

        # Search for ITRequests by title or description
        requests = ITRequest.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

        # Search for ContactPersons by name, email, phone or office location
        contacts = ContactPerson.objects.filter(
            Q(name__icontains=query) | 
            Q(email__icontains=query) | 
            Q(phone__icontains=query) | 
            Q(office_location__icontains=query)
        )

        # Return JSON response with the search results
        return JsonResponse({
            'teams': list(teams.values('id', 'name')),
            'requests': list(requests.values('id', 'title', 'description')),
            'contacts': list(contacts.values('id', 'name', 'email', 'phone', 'office_location', 'team__name'))
        })
    
    # Empty query case, return empty lists
    return JsonResponse({
        'teams': [],
        'requests': [],
        'contacts': []
    })