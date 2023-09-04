from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, EmployeeViewSet, ManagerViewSet,DeviceViewSet, DeviceLogListView, DeviceLogDetailView

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'managers', ManagerViewSet)
router.register(r'devices', DeviceViewSet)

urlpatterns = [
    path('', include(router.urls)),

	path('device-log/', DeviceLogListView.as_view(), name='device-log-list'),
    path('device-log/<int:pk>/', DeviceLogDetailView.as_view(), name='device-log-detail'),
]
