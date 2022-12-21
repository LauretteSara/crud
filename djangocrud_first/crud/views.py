from django.shortcuts import render, redirect
from crud.forms import UtilisateursForm
from crud.models import Utilisateurs
# Create your views here.

def emp(request): 
    form = UtilisateursForm()
    if request.method == "POST":
        form = UtilisateursForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/utilisateurs')
            except:
                pass
        else: 
             form = UtilisateursForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    utilisateurs = Utilisateurs.objects.all()  
    return render(request,"utilisateur.html",{'utilisateurs':utilisateurs})  
def edit(request, id):  
    utilisateurs = Utilisateurs.objects.get(id=id)  
    return render(request,'edit.html', {'utilisateurs':utilisateurs})  
def update(request, id):  
    utilisateurs = Utilisateurs.objects.get(id=id)  
    form = UtilisateursForm(request.POST, instance = utilisateurs)  
    if request.method == 'POST':
        if form.is_valid():  
            form.save()  
            return redirect("/utilisateurs")  
    return render(request, 'edit.html', {'utilisateurs': utilisateurs, 'form': form})  
def destroy(request, id):  
    utilisateurs = Utilisateurs.objects.get(id=id)  
    utilisateurs.delete()  
    return redirect("/utilisateurs")  
        