from django.contrib import admin
from django.urls import path
from tasks.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home, name='home'),
    path('signup/',SignUp, name='signup'),
]
