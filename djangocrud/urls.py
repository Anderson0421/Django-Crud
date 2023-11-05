from django.contrib import admin
from django.urls import path
from tasks.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',helloWorld),
    path('signup/',helloWorld),
]
