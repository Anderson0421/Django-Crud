from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm  #Con esto creamos un formulario de registro
from django.contrib.auth.models import User #Aqui sera donde guardaremos nuestro usuarios en este modelo

def Home(request):
    return render(request,'home.html')

def SignUp(request):
    if request.method =='GET':
        context={
            'form':UserCreationForm()
        }
    else:
        if request.POST['password1'] == request.POST['password2']:
            # Registrar usuario
            # Creamos un objeto el create_user espera como parametro el username y password del formulario
            try:
                user = User.objects.create_user(request.POST['username'],request.POST['password1'])
                user.save() # Lo almacenamos en un formulario y lo guardamos
            except:
                return HttpResponse('El usuario ya existe')
            
            return HttpResponse('User correctamente creado')
        else:
            return HttpResponse('Las contraseñas no coinciden')
    
    
    
    return render(request,'signup.html',context)

