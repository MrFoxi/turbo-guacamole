from django.shortcuts import render, redirect
from django.http import HttpResponse
from preview_app.models import Jour, Salle
from flask import Flask, request
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def planning(request):
    #j'ai accès à la variable "jours" dans le template
    jours = Jour.objects.all()
    salles = Salle.objects.all()
    return render(request, 'planning/planning.html', {'jours': jours, 'salles': salles})
    # return HttpResponse('<h3>PLANNING</h3>')

app = Flask(__name__)

@csrf_exempt
@app.route('/planning_ajout/', methods=['POST'])
def ajout_salle(request):
    # ! is_ajax() => deprecated donc le truc giga long en dessous
    # if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':   
    salles = Salle.objects.all()
    jours = Jour.objects.all()
    nombre = len(salles)
    Salle.objects.create(titre='Salle ' + str(nombre + 1))
    #faut refresh la page mtn
    return render(request, 'planning/planning.html', {'jours': jours, 'salles': salles})
