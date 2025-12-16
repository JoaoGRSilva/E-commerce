from django.shortcuts import render

from .models import Item
from rest_framework import generics
from .serializers import ItemSerializer

class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer