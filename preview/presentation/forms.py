from django import forms
from preview_app.models import Presentation

class PresentationForm(forms.ModelForm):
    class Meta:
        model = Presentation
        fields = ['titre', 'description', 'fichier_pptx', 'id_session']


