#fichier views > to get input form user using webpage and use that input to generate prediction and show that prediction to the user with a web page

from django.shortcuts import render

def home(request):
    return render(request, 'home_page.html')

def result(request):
    pass

def getPredictions():
    import pickle
    model = pickle.load(open("stacking_model.pkl", "rb"))
    pass    
