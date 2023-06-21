from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework import viewsets
from .models import to_do
from .serializers import to_do_Serializer
# Create your views here.
class to_do_viewSet(viewsets.ModelViewSet):
    queryset = to_do.objects.all()
    serializer_class=to_do_Serializer

