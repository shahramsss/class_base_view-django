from django import forms
from .models import Car
from django.forms import modelformset_factory


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"


CarFormSet = modelformset_factory(Car, form=CarCreateForm, extra=3)