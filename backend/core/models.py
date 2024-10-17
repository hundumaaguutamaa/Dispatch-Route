from django.db import models

# Model for IT Team
class ITTeam(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Unique team name

    def __str__(self):
        return self.name

# Model for Contact Person associated with each team
class ContactPerson(models.Model):
    name = models.CharField(max_length=100)  # Contact person's name
    email = models.EmailField()              # Contact person's email
    phone = models.CharField(max_length=15)  # Contact person's phone number
    office_location = models.CharField(max_length=100)  # Office location
    team = models.ForeignKey(ITTeam, on_delete=models.CASCADE, related_name='contacts')  # Team relationship

    def __str__(self):
        return f"{self.name} ({self.team.name})"

# Model for IT Request, linked to the responsible team
class ITRequest(models.Model):
    title = models.CharField(max_length=200)  # Request title
    description = models.TextField()  # Detailed description of the request
    team = models.ForeignKey(ITTeam, on_delete=models.CASCADE, related_name='requests')  # Team responsible for the request


    def __str__(self):
        return self.title

