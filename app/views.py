from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import CohortInfo
from .serializers import CohortInfoSerializer

class CohortInfoListCreate(generics.ListCreateAPIView):
    queryset = CohortInfo.objects.all()
    serializer_class = CohortInfoSerializer

class CohortInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CohortInfo.objects.all()
    serializer_class = CohortInfoSerializer
