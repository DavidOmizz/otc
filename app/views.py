from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import CohortInfo
from .serializers import CohortInfoSerializer
from .utils import send_registration_email  # Import the email function

class CohortInfoListCreate(generics.ListCreateAPIView):
    queryset = CohortInfo.objects.all()
    serializer_class = CohortInfoSerializer

    def perform_create(self, serializer):
        # Save the new cohort info
        instance = serializer.save()
        
        # Send email to the newly registered user
        send_registration_email(instance.email, instance.name)

class CohortInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CohortInfo.objects.all()
    serializer_class = CohortInfoSerializer
