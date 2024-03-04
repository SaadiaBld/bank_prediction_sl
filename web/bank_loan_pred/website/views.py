from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#from .forms import CryptoApiForm, ModelApiForm
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os

# Create your views here.

@login_required
def api_data(request):
    url = 'http://172.17.0.3:8001/predict'

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

            return render(request, "main/api_predict.html", context={'form':form, 'data': data})

    else:
        form = ModelApiForm()

    
    return render(request, "main/api_predict_page.html", context={'form':form})
def home(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def special(request):
    return render(request, 'special.html')

def contact(request):
    return render(request, 'contact.html')

