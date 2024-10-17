from django.contrib import admin
from .models import ITTeam, ContactPerson, ITRequest

# Admin configuration for ITTeam model
class ITTeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']  # Display team ID and name
    search_fields = ['name']  # Enable search by team name

# Admin configuration for ContactPerson model
class ContactPersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'office_location', 'team']  # Display contact details
    list_filter = ['team']  # Enable filtering by team
    search_fields = ['name', 'email', 'team__name']  # Enable search by name, email, or team name

# Admin configuration for ITRequest model
class ITRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']  # Display request ID, title, and description
    search_fields = ['title', 'description']  # Enable search by title or description

# Register the models with the Django admin site
admin.site.register(ITTeam, ITTeamAdmin)
admin.site.register(ContactPerson, ContactPersonAdmin)
admin.site.register(ITRequest, ITRequestAdmin)
