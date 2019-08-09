from django import forms
from .models import *


class ActivityForm(forms.ModelForm):

    class Meta:
        model = Activity
        fields = ['text', 'picture']
