from django.contrib import messages
from django.shortcuts import redirect, render
import bcrypt
from .decorators import login_required,admin_requerido
from .models import User, Quote


@login_required
def index(request):

    context = {
            'usuarios' : User.objects.all(),
            'citas' : Quote.objects.all(),
                    
        }
    return render(request, 'index.html', context)

@admin_requerido
def administrador(request):

    context = {
        'saludo': 'ADMINISTRADOR'
    }
    return render(request, 'admin.html', context)



def quote_post(request):
    if request.method == "GET":

        context = {
            'usuarios' : User.objects.all(),
            'citas' : Quote.objects.all(),
                    
        }

        return render(request, 'index.html', context)


    if request.method == "POST":

        print(request.POST)
        
        errors = Quote.objects.validador_basico(request.POST)
        
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                # print("DESDE EL FOR: ",key, value)

        else:
            cita = Quote.objects.create(
                cita = request.POST['quote'],
                autor = request.POST['quote_author'],
                posteado_por = User.objects.get(id = request.session['usuario']['id'])
                )
            
            messages.success(request,"Exito en agregar la cita")
        
        return redirect('/')



def borrar(request, id):
    id : id
    cita = Quote.objects.get(id=id)
    cita.delete()
    messages.success(request,"Exito en eliminar la cita")
    return redirect(f"/users/{request.session['usuario']['id']}")

def show(request, id):

    context = {
        'id' : id,
        'usuario' : User.objects.get(id=id),
    }
    return render(request, 'usuario_citas.html', context)

def editar(request, id):
    context = {
        'id' : id,
        'usuario': User.objects.get(id=id),
    }
    return render(request, 'editar.html', context)


def update(request, id):
    print(request.POST)


    errores = User.objects.validador_editar(request.POST)
    print(errores)

    if len(errores) > 0:
        # si el diccionario de errores contiene algo, recorra cada par clave-valor y cree un mensaje flash
        for key, value in errores.items():
            messages.error(request, value)

        context = {
            'id' : id,
            'usuario': User.objects.get(id=id),
            }

        request.session['editar_name']=request.POST['name']
        request.session['editar_apellido']=request.POST['apellido']
        request.session['editar_email']=request.POST['email']


        # redirigir al usuario al formulario para corregir los errores
        return render(request, 'editar.html', context)

    else:

        request.session['editar_name']=''
        request.session['editar_apellido']=''
        request.session['editar_email']=''

        usuario = User.objects.get(id=id)
        usuario.name=request.POST['name']
        usuario.apellido=request.POST['apellido']
        usuario.email=request.POST['email']
        usuario.save()
        messages.success(request,"Exito en editar el usuario")
        return redirect("/logout")
