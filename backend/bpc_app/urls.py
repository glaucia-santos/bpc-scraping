from django.urls import path, include
from rest_framework import routers
from .views import BPCRegistroViewSet
from rest_framework.response import Response
from .views import StatusAPIView



router = routers.DefaultRouter()
router.register(r'bpc', BPCRegistroViewSet, basename='bpc')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/status/', StatusAPIView.as_view()),
]
