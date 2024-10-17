import django_filters
from .models import ITRequest

# Custom filter for ITRequest model
class ITRequestFilter(django_filters.FilterSet):
    class Meta:
        model = ITRequest
        fields = ['team__name']  # Filter by team name and status
