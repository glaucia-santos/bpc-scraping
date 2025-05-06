from django.urls import path, include
from rest_framework import routers
from .views import BPCRegistroViewSet
from rest_framework.response import Response

router = routers.DefaultRouter()
router.register(r'bpc', BPCRegistroViewSet, basename='bpc')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/status/', lambda req: Response({'status': 'online'})),
]
