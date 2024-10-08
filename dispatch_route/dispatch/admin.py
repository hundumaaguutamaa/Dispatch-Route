# dispatch/admin.py
from django.contrib import admin
from .models import Team, Request

# Register the Team model
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']  # Display these fields in the admin list view

# Register the Request model
@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'assigned_team']  # Display fields
    search_fields = ['description']  # Add a search bar for description
    list_filter = ['assigned_team']  # Filter by assigned team in the sidebar

