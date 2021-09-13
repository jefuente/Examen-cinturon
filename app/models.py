from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def validador_basico(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        SOLO_LETRAS = re.compile(r'^[a-zA-Z. ]+$')

        errors = {}

        if len(postData['name']) < 2:
            errors['name_len'] = "nombre debe tener al menos 2 caracteres de largo";

        if len(postData['apellido']) < 2:
            errors['apellido_len'] = "apellido debe tener al menos 2 caracteres de largo";

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "correo invalido"

        if not SOLO_LETRAS.match(postData['name']):
            errors['solo_letras_name'] = "solo letras en nombre porfavor"
        
        if not SOLO_LETRAS.match(postData['apellido']):
            errors['solo_letras_apellido'] = "solo letras en apellido porfavor"

        if len(postData['password']) < 8:
            errors['password'] = "contraseña debe tener al menos 8 caracteres";

        if postData['password'] != postData['password_confirm'] :
            errors['password_confirm'] = "contraseña y confirmar contraseña no son iguales. "

        
        return errors

    def validador_editar(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        SOLO_LETRAS = re.compile(r'^[a-zA-Z. ]+$')

        errors = {}

        if len(postData['name']) < 2:
            errors['name_len'] = "nombre debe tener al menos 2 caracteres de largo";

        if len(postData['apellido']) < 2:
            errors['apellido_len'] = "apellido debe tener al menos 2 caracteres de largo";

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "correo invalido"

        #usuarios = User.objects.all()
        #if postData['email'] != request.session['usuario']['email']:
            #for u in usuarios:
                #if postData['email'] ==u.email:
                    #errors['email_unico'] = "email debe ser unico, este ya fue ingresado por otro usuario";

        return errors


class User(models.Model):
    CHOICES = (
        ("user", 'User'),
        ("admin", 'Admin')
    )
    name = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    role = models.CharField(max_length=255, choices=CHOICES)
    password = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    #citas_posteadas = Usuarios tienen citas posteadas
    #me_gusta = Usuarios tienen me gusta

    def __str__(self):
        return f"{self.name} {self.apellido}"

    def __repr__(self):
        return f"{self.name} {self.apellido}"


class QuoteManager(models.Manager):
    def validador_basico(self, postData):

        errors = {}

        if len(postData['quote_author']) < 2:
            errors['autor_len'] = "autor debe tener al menos 2 caracteres de largo";

        if len(postData['quote']) < 2:
            errors['cita_len'] = "cita debe tener al menos 2 caracteres de largo";

 
        return errors        

class Quote(models.Model):
    cita = models.CharField (max_length=255, null = True)
    autor = models.CharField (max_length=255, null = True)
    posteado_por = models.ForeignKey(User, related_name="citas_posteadas", on_delete=models.CASCADE)
    megusta_users = models.ManyToManyField(User, related_name="me_gusta")
    created_at = models.DateTimeField (auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = QuoteManager()



#class Like(models.Model):
    #posteado_por = models.ForeignKey(User, related_name="citas_posteadas", on_delete=models.CASCADE)
    #cita =  models.ForeignKey(Quote, related_name ="likes") 
    #created_at = models.DateTimeField (auto_now_add = True)
    #updated_at = models.DateTimeField(auto_now=True)