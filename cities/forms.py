from django import forms
from .models import Restaurants

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurants
        fields = ['name', 'specialization', 'address', 'website', 'phone_number']

class SpecializationForm(forms.Form):
    SPECIALIZATION_CHOICES = [
        ('', 'All'),
        ('Italian', 'Italian'),
        ('French', 'French'),
        ('Asian', 'Asian'),
        ('Family', 'Family'),
        ('Other', 'Other'),
    ]
    specialization = forms.ChoiceField(choices=SPECIALIZATION_CHOICES, required=False)