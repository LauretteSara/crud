from django.shortcuts import render, redirect
from crud.forms import UtilisateursForm
from crud.models import Utilisateurs
# Create your views here.

def emp(request): 
    form = UtilisateursForm()
    erreur = ""
    if request.method == "POST":
        form = UtilisateursForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else: 
             erreur = form.errors
    context = {'form':form, 'erreur':erreur}
    return render(request,'index.html', context)  


def show(request):  
    utilisateurs = Utilisateurs.objects.all()  
    return render(request,"utilisateur.html",{'utilisateurs':utilisateurs})  


def edit(request, id):  
    utilisateurs = Utilisateurs.objects.get(id=id)  
    return render(request,'edit.html', {'utilisateurs':utilisateurs})  


def update(request, id):  
    utilisateurs = Utilisateurs.objects.get(id=id)  
    form = UtilisateursForm( instance = utilisateurs)  
    if request.method == 'POST':
        form = UtilisateursForm(request.POST, request.FILES,instance = utilisateurs)
        if form.is_valid():  
            form.save()  
            return redirect("../")  
    return render(request, 'index.html', {'utilisateurs': utilisateurs, 'form': form})  


def destroy(request, id):  
    utilisateurs = Utilisateurs.objects.get(id=id)  
    utilisateurs.delete()  
    return redirect("/")  
        