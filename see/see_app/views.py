from django.shortcuts import render
from see_app.models import Perfilempresa

# Create your views here.

def inicio(request):
    recomendados=Perfilempresa.objects.all()
    data={"recomendados":recomendados}
    return render(request, "see_app/inicio.html", data)

def registrar_usuario():
    pass

def crear_perfil_empresa():
    pass

def logear_usuario():
    pass

def logout():
    pass

def buscar_empresa():
    pass

def ver_pefil_empresa():
    pass

def ver_ficha_estadisticas():
    pass
