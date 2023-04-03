from django.shortcuts import render, redirect
from preview_app.models import Jour, Salle
from flask import Flask, request

app = Flask(__name__)

#permet de rajouter une salle quand on click sur un bouton "+"
@app.route('/planning/scripts.py', methods=['POST'])
def ajout_salle():

    salles = Salle.objects.all()
    nombre = len(salles)
    Salle.objects.create(titre='Salle ' + str(nombre + 1))
    #peut marcher mais pas sur
    return redirect('planning/planning.html')

if __name__ == '__main__':
    app.run()
