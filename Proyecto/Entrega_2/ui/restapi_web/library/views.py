from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return render(request, 'ml/index.html')

def process(request):
    return render(request, 'ml/process.html')

def inference(request):
    return render(request, 'ml/inference.html')

def train(request):
    return render(request, 'ml/train.html')

def save_data(request):
    return render(request, 'ml/save_data.html')