from django import forms
from .models import Volunteer

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['event', 'user', 'role', 'shift_start', 'shift_end', 'status', 'notes']
