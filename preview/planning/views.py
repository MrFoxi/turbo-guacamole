from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from preview_app.models import Jour, Salle
from flask import Flask, request
from django.views.decorators.csrf import csrf_exempt
from conference.forms import SessionForm

# * Page planning
def planning(request):
    #j'ai accès à la variable "jours" dans le template
    jours = Jour.objects.all()
    salles = Salle.objects.all()
    form = SessionForm(request.POST)
    return render(request, 'planning/planning.html', {'form': form,'jours': jours, 'salles': salles})
    # return HttpResponse('<h3>PLANNING</h3>')

app = Flask(__name__)





# * Ajout d'une salle 
@csrf_exempt
@app.route('/planning_ajout/', methods=['POST'])
def ajout_salle(request):
    salles = Salle.objects.all()
    jours = Jour.objects.all()
    nombre = len(salles)
    Salle.objects.create(titre='Salle ' + str(nombre + 1))
    #faut refresh la page mtn
    return render(request, 'planning/planning.html', {'jours': jours, 'salles': salles})

# * Modification du titre d'une salle
@csrf_exempt
@app.route('/planning_update/', methods=['POST'])
def update_text(request):
    if request.method == "POST":
        updated_text = request.POST.get("text", "")
        id_salle = request.POST.get("id", "")
        if updated_text == "":
            updated_text = "Salle"
        # Faites ici quelque chose avec le texte mis à jour, comme l'enregistrer en base de données
        Salle.objects.filter(id=id_salle).update(titre=updated_text)
        return JsonResponse({"success": True})
    else:
        return JsonResponse({"success": False})
    


def jour(request):

    select = False

    all_jours = Jour.objects.all()

    context = {'select': select, 'all_jours': all_jours}
    
    return render(request, 'ajout/gestion.html', context)

def salle(request):

    select = False

    all_salles = Salle.objects.all()
    print(all_salles)
    
    context = {'select': select, 'all_salles': all_salles}

    return render(request, 'ajout/gestion.html', context)


def salle_detail(request, salle_id):
    
    select = True

    all_salles = Salle.objects.all()
    
    salle_choose = Salle.objects.get(id=salle_id)

    # votre logique pour récupérer les détails de la salle et le formulaire associé

    context = {'select': select, 'salle_choose':salle_choose,'all_salles':all_salles,'salle_id': salle_id}

    return render(request, 'ajout/gestion.html', context)

def jour_detail(request, jour_id):

    select = True

    all_jours = Jour.objects.all()
    
    jour_choose = Jour.objects.get(id=jour_id)
    print(jour_choose)

    # votre logique pour récupérer les détails de la salle et le formulaire associé

    context = {'select': select, 'jour_choose':jour_choose,'all_jours':all_jours,'jour_id': jour_id}

    return render(request, 'ajout/gestion.html', context)