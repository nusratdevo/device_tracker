from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, EmployeeViewSet, ManagerViewSet,DeviceViewSet, DeviceLogListView, DeviceLogDetailView,CompanyDevice

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'managers', ManagerViewSet)
router.register(r'devices', DeviceViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title="Device Tracker API",
        default_version='v1',
        description="API Description",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
)

urlpatterns = [
    path('', include(router.urls)),

	path('device-log/', DeviceLogListView.as_view(), name='device-log-list'),
    path('device-log/<int:pk>/', DeviceLogDetailView.as_view(), name='device-log-detail'),
    path('company-device/<company_id>/', CompanyDevice.as_view()),

	
# api Autometed documentation urls
	path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
