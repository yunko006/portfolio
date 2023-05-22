from rest_framework import generics
from .models import ProjetPro
from .serializers import ProjetProtSerializer


class ProjetProList(generics.ListCreateAPIView):
    queryset = ProjetPro.objects.all()
    serializer_class = ProjetProtSerializer


class ProjetProDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjetPro.objects.all()
    serializer_class = ProjetProtSerializer
