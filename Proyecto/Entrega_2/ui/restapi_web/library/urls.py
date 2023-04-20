from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('process', views.process, name='process'),
    path('inference', views.inference, name='inference'),
    path('train', views.train, name='train'),
    path('save', views.save_data, name='save')
]