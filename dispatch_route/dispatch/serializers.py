# dispatch/serializers.py
from rest_framework import serializers
from .models import Team, Request

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name']

class RequestSerializer(serializers.ModelSerializer):
    assigned_team = TeamSerializer(read_only=True)
    assigned_team_id = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), source='assigned_team', write_only=True)

    class Meta:
        model = Request
        fields = ['id', 'description', 'assigned_team', 'assigned_team_id']
