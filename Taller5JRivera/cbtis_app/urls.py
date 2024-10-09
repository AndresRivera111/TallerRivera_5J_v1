from django.urls import path, include
from cbtis_app import views

urlpatterns = [
    path('',views.verLista, name='verLista'),
]