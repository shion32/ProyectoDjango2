from django.shortcuts import render
from .models import Tareas

def home(request):
    tareas=Tareas.objects.all()
    context={"tareas":tareas}
    return render(request,"todo/home.html",context)

# Create your views here.
