from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import generics
from .models import Company, Employee, Manager, Device, DeviceLog
from .serializers import CompanySerializer, EmployeeSerializer, ManagerSerializer, DeviceSerializer, DeviceLogSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceLogListView(generics.ListCreateAPIView):
    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer

class DeviceLogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer
    