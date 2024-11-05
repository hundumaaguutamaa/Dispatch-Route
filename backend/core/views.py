from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import ITTeam, ContactPerson, ITRequest
from .serializers import ITTeamSerializer, ContactPersonSerializer, ITRequestSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse
from django.db.models import Q

# ViewSet for ITTeam
class ITTeamViewSet(viewsets.ModelViewSet):
    queryset = ITTeam.objects.all().order_by('name')  # Ensure the queryset is ordered
    serializer_class = ITTeamSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']

# ViewSet for ContactPerson
class ContactPersonViewSet(viewsets.ModelViewSet):
    queryset = ContactPerson.objects.all().order_by('name')  # Ensure the queryset is ordered
    serializer_class = ContactPersonSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['team__name']
    search_fields = ['name', 'email']

# ViewSet for ITRequest
class ITRequestViewSet(viewsets.ModelViewSet):
    queryset = ITRequest.objects.all().order_by('title')  # Ensure the queryset is ordered
    serializer_class = ITRequestSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['team__name']
    search_fields = ['title', 'description']

def search(request):
    query = request.GET.get('q', '')
    if query:
        # Search for ITTeams by name
        teams = ITTeam.objects.filter(name__icontains=query).order_by('name')

        # Search for ITRequests by title or description
        requests = ITRequest.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        ).order_by('title')

        # Search for ContactPersons by name, email, phone or office location
        contacts = ContactPerson.objects.filter(
            Q(name__icontains=query) | 
            Q(email__icontains=query) | 
            Q(phone__icontains=query) | 
            Q(office_location__icontains=query)
        ).order_by('name')

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
