from django.shortcuts import render
from rest_framework import viewsets

from zip.models import ZipCode
from zip.serializers import ZipCodeSerializer


# Create your views here.
class ZipCodeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ZipCode.objects.all()
    serializer_class = ZipCodeSerializer
