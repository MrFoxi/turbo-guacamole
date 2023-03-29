from django.http import HttpResponse
from django.shortcuts import render, redirect
from preview_app.models import Conference, Jour
from conference.forms import ConferenceForm
from datetime import timedelta

def index(request):
    if request.method == 'POST':
        form = ConferenceForm(request.POST, request.FILES)
        if form.is_valid():
            conference = form.save(commit=False)
            conference.save()

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
        return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')
    else:
        return render(request ,'conference/conference.html', {'form': form})