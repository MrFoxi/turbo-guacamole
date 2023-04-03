from django.shortcuts import render, redirect
from preview_app.models import Presentation

# Create your views here.

def presentation(request):
    presentation = Presentation.objects.all()
    return render(request ,'presentation/presentation.html')