from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver



class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Manager(models.Model):
    name = models.CharField(max_length=100)
    company = models.OneToOneField(Company, on_delete=models.CASCADE, related_name='manager')

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return self.name

class Device(models.Model):
    name = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    checked_out = models.DateTimeField(null=True, blank=True)
    checked_in = models.DateTimeField(null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='devices')
    assigned_employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
    
class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    condition = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.device.name} - {self.timestamp}"


