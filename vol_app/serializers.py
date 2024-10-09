# vol_app/serializers.py
from rest_framework import serializers
from .models import Volunteer

class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = ['name', 'email', 'role', 'shift_start', 'shift_end']  # Include necessary fields only

    # Example of custom validation (optional)
    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("Email is required.")
        return value

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name is required.")
        return value
