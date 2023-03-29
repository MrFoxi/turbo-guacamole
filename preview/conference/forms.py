from django import forms

from django.forms.widgets import SelectMultiple
from preview_app.models import Conference, Jour


class ConferenceForm(forms.ModelForm):
    debut = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    fin = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Conference
        fields = '__all__' # supprimez cette ligne


