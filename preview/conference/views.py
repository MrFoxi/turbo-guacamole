from django.http import HttpResponse
from django.shortcuts import render, redirect
from preview_app.models import Conference, Jour, Salle
from conference.forms import ConferenceForm
from datetime import timedelta
from django.urls import reverse


def accueil(request):
    accueil_exists = True
    return render(request, 'conference/accueil.html' , {'accueil_exists': accueil_exists})

def index(request):
    # On prend la liste des jours pour afficher le form de conference ou pas s'il y'en a
    jours_existants = Jour.objects.all()
    conference_exists = False
    if request.method == 'POST':
        form = ConferenceForm(request.POST, request.FILES)
        if form.is_valid():
            conference = form.save(commit=False)
            conference.save()


            # Créer la salle par défaut pour un planning simple et en ajouter par la suite
            Salle.objects.create(titre='Salle 1')

            debut = form.cleaned_data.get('debut')
            fin = form.cleaned_data.get('fin')

            # Créer tous les jours entre debut et fin
            jours = []
            jour = debut
            while jour <= fin:
                jours.append(jour)
                jour += timedelta(days=1)

            # Ajouter les jours à la conférence
            for jour in jours:
                Jour.objects.create(date=jour)

            return redirect('conference')
    else:
        form = ConferenceForm()

    if Conference.objects.exists():
        # return render(request, '../../planning/templates/planning/base.html')
        jours = Jour.objects.all()
        url = reverse('planning')
        conference_exists = True
        return redirect(url)
    else:
        return render(request ,'conference/conference.html', {'form': form, 'jours_existants': jours_existants, 'conference_exists': conference_exists})