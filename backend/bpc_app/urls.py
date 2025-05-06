from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

def status_view(request):
    return JsonResponse({'status': 'online'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/status/', status_view),
]
