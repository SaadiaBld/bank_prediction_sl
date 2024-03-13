from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ModelApiForm
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os



@login_required
def api_data(request):
    url = ''

    headers = {
    'Accepts': 'application/json',
    }

    session = Session()
    session.headers.update(headers)

        # si c'est une requete post , on doit process les données 
    if request.method == "POST":
        # cree un form rempli avec les données de requête
        form = ModelApiForm(request.POST)
        # verifie si form est valide
        if form.is_valid():
            print(form.cleaned_data)
            
            features = json.dumps(form.cleaned_data)
            response = session.post(url, data=features)
            data = json.loads(response.text)
            form.save()
            print('ok')

            return render(request, "website/api_data.html", context={'form':form, 'data': data})

    else:
        form = ModelApiForm()

    
    return render(request, "website/api_data.html", context={'form':form})

def home(request):
    return render(request, 'website/index.html')

def aboutus(request):
    return render(request, 'website/aboutus.html')

def contact(request):
    return render(request, 'website/contact.html')

def api_url():
    return (os.getenv('API_URL'))

@login_required
def special(request):
    return render(request, 'website/special.html')

@login_required
def predict(request):

    url = 'http://localhost:8001/predict'

    headers = {
    'Accepts': 'application/json',
    }

    session = Session()
    session.headers.update(headers)

        # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ModelApiForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print(form.cleaned_data)
            
            features = json.dumps(form.cleaned_data)
            response = session.post(url, data=features)
            data = json.loads(response.text)
            form.save()
            print('ok')
            category=data['category'] #extrait la valeur du dico data = {category: 0 ou 1}
            return render(request, "website/predict.html", context={'form':form, 'data': data, "category":category} )

    else:
        form = ModelApiForm()

    
    return render(request, "website/predict.html", context={'form':form})

