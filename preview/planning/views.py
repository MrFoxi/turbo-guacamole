from django.shortcuts import render
from django.http import HttpResponse
from preview_app.models import Jour


# Create your views here.
def planning(request):
    #j'ai accès à la variable jour dans le template
    jours = Jour.objects.all()
    return render(request, 'base.html', {'jours': jours})
    # return HttpResponse('<h3>PLANNING</h3>')
