from django.shortcuts import render,HttpResponse
import requests

# Create your views here.
def DemoView(request):
    return HttpResponse("<h1>Demo View</h1>")

def index(request):
    color = ['red', 'blue', 'green']
    context = {'color':color}
    return render(request, 'index.html', context)

def api_data(request):
    url = "https://restcountries.eu/rest/v2/all"
    data = requests.get(url).json()
    context = {'data':data}
    return render(request, 'apidata.html', context)
