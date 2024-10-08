from django.db import models

# Create your models here.
# dispatch/models.py
from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Request(models.Model):
    description = models.CharField(max_length=200)
    assigned_team = models.ForeignKey(Team, related_name='requests', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.description} ({self.assigned_team.name})"
