from django import forms
from .models import *

class LeaveApplicationForm(forms.ModelForm):

    class Meta:
        model = LeaveApplication
        fields = "__all__"