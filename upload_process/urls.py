from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from upload_process.views import homePage

urlpatterns = [
    path('', homePage, name='home')
]