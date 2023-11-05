from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm  #Con esto creamos un formulario de registro

def Home(request):
    return render(request,'home.html')



def SignUp(request):
    context={
        'form':UserCreationForm()
    }
    return render(request,'signup.html',context)