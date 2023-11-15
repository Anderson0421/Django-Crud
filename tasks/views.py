from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm #Con esto creamos un formulario de registro
from django.contrib.auth.models import User #Aqui sera donde guardaremos nuestro usuarios en este modelo
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
def Home(request):
    return render(request,'home.html')

def SignUp(request):
    if request.method =='GET':
        return render(request,'signup.html',{
            'form':UserCreationForm()
        })
    
    else:
        if request.POST['password1'] == request.POST['password2']:
            # Registrar usuario
            # Creamos un objeto el create_user espera como parametro el username y password del formulario
            try:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save() # Lo almacenamos en un formulario y lo guardamos
                login(request,user)
                return redirect('/task')
            except:
                return render(request,'signup.html',{
                    'form':UserCreationForm(),
                    'error':"El usuario ya existe"
                })
        return render(request,'signup.html',{
                    'form':UserCreationForm(),
                    'error':"Las contrasenas no coinciden"
                })    


@login_required(login_url='/signup/')
def Tasks(request):
    return render(request,'task.html')