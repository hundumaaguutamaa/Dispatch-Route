from django.shortcuts import render

# Create your views here.
# dispatch/views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Team, Request
from .serializers import TeamSerializer, RequestSerializer

# Add a new team
class TeamCreateView(generics.CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamListView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

# Add a new IT request
class RequestCreateView(generics.CreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

# Search for requests or teams by query
@api_view(['GET'])
def search(request):
    query = request.query_params.get('q', '')
    team_results = Team.objects.filter(name__icontains=query)
    request_results = Request.objects.filter(description__icontains=query)
    
    teams = TeamSerializer(team_results, many=True).data
    requests = RequestSerializer(request_results, many=True).data

    return Response({'teams': teams, 'requests': requests})
