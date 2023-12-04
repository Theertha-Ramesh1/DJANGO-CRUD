from django import forms
from App3.models import *
class Loginform(forms.ModelForm):
    class Meta:
        model = Login
        fields = "__all__"
