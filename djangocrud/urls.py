from django.contrib import admin
from django.urls import path,include
from tasks.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home, name='home'),
    path('signup/',SignUp, name='signup'),
    path('task/',Tasks, name='task'),

    path("account/", include("django.contrib.auth.urls")),  

]
