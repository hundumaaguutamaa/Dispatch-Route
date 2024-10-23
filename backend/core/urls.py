from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ITTeamViewSet, ContactPersonViewSet, ITRequestViewSet
from . import views

# Define the router to automatically generate routes for viewsets
router = DefaultRouter()
router.register(r'teams', ITTeamViewSet, basename='itteam')  # Routes for IT Teams
router.register(r'contacts', ContactPersonViewSet, basename='contactperson')  # Routes for Contact Persons
router.register(r'requests', ITRequestViewSet, basename='itrequest')  # Routes for IT Requests

# Include the router's URL patterns into the project
urlpatterns = [
    path('', include(router.urls)),  # API root for all routes
    path('search/', views.search, name='search'),
]
