from django.urls import path, include
from rest_framework import routers
from .views import StudentViewSet
from .views import RegisterAPI
from .views import ChangePasswordView
from django.urls import path

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]




