from django.shortcuts import render

from rest_framework import viewsets
from G_artiste.serializers import ArtisteSerializer
from G_artiste.models import  Artiste

# Create your views here.

class CrudArtiste(viewsets.ModelViewSet):
    queryset= Artiste.objects.all()
    serializer_class= ArtisteSerializer
    
