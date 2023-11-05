from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm  #Con esto creamos un formulario de registro

def helloWorld(request):
    context={
        'form':UserCreationForm()
    }
    return render(request,'signup.html',context)