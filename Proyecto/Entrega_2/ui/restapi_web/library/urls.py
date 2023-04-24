from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('process', views.process, name='process'),
    path('inference', views.inference, name='inference'),
    path('train', views.train, name='train'),
    path('save', views.save_data, name='save'),
    path('processed', views.send_data, name='processed'),
    path('trainned', views.train_data, name='trainned'),
    path('saved', views.save_ok, name='saved'),
    path('inferenced', views.inference_ok, name='inferenced')
]