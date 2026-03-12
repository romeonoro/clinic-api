from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework.routers import DefaultRouter

from patients.views import PatientViewSet
from doctors.views import DoctorViewSet
from appointments.views import AppointmentViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny


# Swagger configuration
schema_view = get_schema_view(
    openapi.Info(
        title="Clinic API",
        default_version='v1',
        description="API para gerenciamento de consultas médicas",
    ),
    public=True,
    permission_classes=[AllowAny],
)

# Router da API
router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # API routes
    path('api/', include(router.urls)),

    # Swagger docs
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0)),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0)),
]