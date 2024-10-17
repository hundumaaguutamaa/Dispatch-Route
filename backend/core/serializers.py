from rest_framework import serializers
from .models import ITTeam, ContactPerson, ITRequest

# Serializer for IT Team model
class ITTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ITTeam
        fields = '__all__'  # Serialize all fields in the ITTeam model

# Serializer for Contact Person model
class ContactPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPerson
        fields = '__all__'  # Serialize all fields in the ContactPerson model

# Serializer for IT Request model
class ITRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ITRequest
        fields = '__all__'  # Serialize all fields in the ITRequest model
