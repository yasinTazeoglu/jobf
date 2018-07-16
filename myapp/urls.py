from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include('job.urls'),name='job'),
    path('admin/', admin.site.urls),
]
