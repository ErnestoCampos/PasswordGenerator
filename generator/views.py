from django.shortcuts import render
import random
from random import choice
# Create your views here.

def home(request):
    return render(request, "home.html")

def password(request):
    characters = list("abcdefghijklmnopqrstuvwxyz")
    generated_password = ""

    lenght = int(request.GET.get("lenght"))
    
    if request.GET.get("uppercase"):
      characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    if request.GET.get("numbers"):
      characters.extend(list("0123456789"))

    if request.GET.get("symbols"):
      characters.extend(list("!#$%&/()=[:_"))

    for char in range(lenght):
        generated_password += random.choice(characters)



    return render(request, "password.html", {"password":generated_password})