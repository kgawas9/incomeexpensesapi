from django.http import request
from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions

from .serializers import ExpenseSerializer
from .models import Expense
from .permissions import IsOwner
# Create your views here.

class ExpenseListAPIView(ListCreateAPIView):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        # print(self.request.user)
        return self.queryset.filter(owner=self.request.user)

class ExpenseDtailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer
    
    permission_classes = (permissions.IsAuthenticated, IsOwner, )
    queryset = Expense.objects.all()

    lookup_field = 'id'

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

