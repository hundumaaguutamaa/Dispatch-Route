from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from core import views  # Import views from the core app where your viewsets are defined

# You can define a router here to use with ViewSets
# If using ViewSets, define routers like this
router = routers.DefaultRouter()
router.register(r'teams', views.ITTeamViewSet)
router.register(r'contacts', views.ContactPersonViewSet)
router.register(r'requests', views.ITRequestViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin route for managing models
    path('api/', include('core.urls')),  # Include app-level URLs
]
