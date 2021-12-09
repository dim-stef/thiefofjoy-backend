from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework import routers, serializers, viewsets
from . import views

router = routers.DefaultRouter()
router.register(r'gratitude_notes', views.GratitudeNoteViewset)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls')),
    path('token/', obtain_jwt_token),
    path('token_refresh/', refresh_jwt_token),
]
