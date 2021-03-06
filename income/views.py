from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions

from .serializers import IncomeSerializer
from .models import Income
from .permissions import IsOwner
# Create your views here.

class IncomeListAPIView(ListCreateAPIView):
    serializer_class = IncomeSerializer
    queryset = Income.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

class IncomeDtailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = IncomeSerializer
    
    permission_classes = (permissions.IsAuthenticated, IsOwner, )
    queryset = Income.objects.all()

    lookup_field = 'id'

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

