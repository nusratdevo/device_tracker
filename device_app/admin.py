from django.contrib import admin

from .models import Company, Employee, Device, Manager, DeviceLog
# Register your models here.

# company Admin registe
class CompanyAdmin(admin.ModelAdmin):
    list = ('name')
    admin.site.register(Company)
    
# Manager Admin registe
class ManagerAdmin(admin.ModelAdmin):
    list = ('name', 'company')
    admin.site.register(Manager)
    
# # Employee Admin registe
class EmployeeAdmin(admin.ModelAdmin):
    list = ('name', 'company')
    admin.site.register(Employee)
    
# # Device Admin registe
class DeviceAdmin(admin.ModelAdmin):
    list = ('name', 'condition', 'checked_in', ' checked_out', 'company',  'assigned_employee')
    admin.site.register(Device)

 # DeviceLog Admin registe 
class DeviceLogAdmin(admin.ModelAdmin):
    list = ('id','device', 'condition', 'timestamp')
    admin.site.register(DeviceLog)
    
