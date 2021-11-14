from django import forms
from .models import details
class detaisform(forms.ModelForm):
    class Meta:
        model = details
        fields = "__all__"