from lib2to3.fixes.fix_input import context
from operator import index
from django.shortcuts import render, HttpResponse
from .models import Employee, Store


# Create your views here.
def viewshtml(request):
        wartosc_z_db = Employee.objects.all()
        return render(request, 'index.html', context = {"zmienna": wartosc_z_db})

def viewszid(request, id):
        wartosc_pojedyncza_z_db = Store.objects.get(id=id)
        return HttpResponse(f"{wartosc_pojedyncza_z_db} / {wartosc_pojedyncza_z_db.location}")