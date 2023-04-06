from django.shortcuts import render, redirect
from preview_app.models import Presentation, InterPresent
from presentation.forms import PresentationForm
import socket
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from flask import Flask, request

app = Flask(__name__)

# Create your views here.

def presentation(request):
    presentations = Presentation.objects.all().prefetch_related('interpresent_set__id_intervenant')
    # print('hello')
    return render(request ,'presentation/presentation.html', {'presentations': presentations})


def add_presentation(request):
    if request.method == 'POST':
        form = PresentationForm(request.POST, request.FILES)
        if form.is_valid():
            presentation = form.save()
            # Do something with the saved presentation
    else:
        form = PresentationForm()
    return render(request, 'presentation/add_presentation.html', {'form': form})

def open_ppt(host, ppt_file):
    host = host
    port = 5000
    message = f"open_ppt@{ppt_file}".encode()
    # create socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # connect to server
        sock.connect((host, port))
        # send string to server
        sock.sendall(message)
        # get server response
        response = sock.recv(1024)
        # decode the response and return it
        return response.decode()


def button_open_pptx(request):
    presentation_id = request.POST.get('presentation_id')
    print('Le formulaire a été soumis avec la valeur presentation_id :', presentation_id)

    presentation = Presentation.objects.get(id=presentation_id)
    fichier_pptx = presentation.fichier_pptx
    print("C:\\Users\\conta\\Desktop\\Python\\InterfaceLocale\\preview\\"+fichier_pptx)
    # open_ppt("192.168.0.157", "C:\\Users\\conta\\Desktop\\Python\\InterfaceLocale\\preview\\"+fichier_pptx)
    print('hello')
    return redirect('presentation')
    # return render(request, 'presentation/presentation.html', {})