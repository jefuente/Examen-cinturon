from django.urls import path
from . import views, auth
urlpatterns = [
    path('', views.index), 
    path('administrador/', views.administrador), 
    path('registro/', auth.registro),
    path('login/', auth.login),
    path('logout/', auth.logout),

    path('quote_post', views.quote_post),
    path('users/<int:id>', views.show),
    path('destroy/<int:id>', views.borrar),
    path('edit/<int:id>', views.editar),
    path('update/<int:id>', views.update),
    
]
