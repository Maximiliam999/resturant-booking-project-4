from django import forms 
from .models import Cancel

class CancelForm(forms.ModelForm):
    class Meta:
        model = Cancel
        fields = ('name', 'phone', 'date')