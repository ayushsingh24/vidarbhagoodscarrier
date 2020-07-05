from django import forms
from .models import Booking

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["name","from_where","to_where","email","phone"]
