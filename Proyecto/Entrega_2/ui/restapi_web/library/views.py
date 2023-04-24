import requests
import library.logger as log
from django.shortcuts import render, redirect
from django.http import HttpResponse
from library.processed import Processed
from library.trainned import Trainned
from library.inference import InferenceModel
from django.contrib import messages
from library.env import URL_PROCESS_DATA, URL_TRAIN, URL_SAVE_DATA, URL_PREDICT_MODEL

logger = log.get_logger('views')

# Create your views here.


def index(request):
    return render(request, 'ml/index.html')

def process(request):
    if request.POST:
       form_p = Processed(request.POST)
       if form_p.is_valid():
           data_type = request.POST["conjunto_de_datos"]
           r = requests.get(URL_PROCESS_DATA, params={'data' : data_type}) 
           logger.info('Parametro data:::%s', data_type)
           if r.status_code == 200:
                return redirect('processed')
           else:
               messages.error(request, 'Ocurrio un Error procesando el conjunto de datos')
    else:
        form_p = Processed()
    return render(request, 'ml/process.html', {'formulario': form_p})

def inference(request):
    if request.POST:
       form_t = InferenceModel(request.POST)
       if form_t.is_valid():
           r = requests.post(url=URL_TRAIN, json={ 'elevation' : request.POST["elevation"],
                'slope': request.POST["slope"],
                'horizontal_distance_to_hidrology' : request.POST["horizontal_distance_to_hidrology"],
                'vertical_distance_to_hidrology' : request.POST["elevation"],
                'horizontal_distance_to_roadways' : request.POST["vertical_distance_to_hidrology"],
                'hillshade_9_am' : request.POST["hillshade_9_am"],
                'hillshade_noon' : request.POST["hillshade_noon"],
                'horizontal_distance_to_firepoints' : request.POST["horizontal_distance_to_firepoints"],
                'wilderness_area' : request.POST["wilderness_area"]
            }) 
           if r.status_code == 200:
                return redirect('inferenced')
           else:
               messages.error(request, 'Ocurrio un Error en el proceso de inferencia')
    else:
        form_t = InferenceModel()
    return render(request, 'ml/inference.html', {'formulario': form_t})

def train(request):
    if request.POST:
       form_t = Trainned(request.POST)
       if form_t.is_valid():
           data_type = request.POST["modelos"]
           r = requests.get(URL_TRAIN, params={'model' : data_type}) 
           logger.info('Parametro model:::%s', data_type)
           if r.status_code == 200:
                return redirect('trainned')
           else:
               messages.error(request, 'Ocurrio un Error en el proceso de entrenamiento del modelo')
    else:
        form_t = Trainned()
    return render(request, 'ml/train.html', {'formulario': form_t})

def save_data(request):
    return render(request, 'ml/save_data.html')

def send_data(request):
    return render(request, 'ml/processed.html')

def train_data(request):
    return render(request, 'ml/trainned.html')

def save_ok(request):
    r = requests.get(URL_SAVE_DATA)
    if r.status_code != 200:
        messages.error(request, 'Ocurrio un Error persistiendo datos de las caracteristicas para hacer inferencia')
        return redirect('save')
    return render(request, 'ml/saved.html')

def inference_ok(request):
    return render(request, 'ml/inferenced.html')