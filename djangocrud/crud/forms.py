from django import forms 
from crud.models import Utilisateurs

# formulaire pour creer un utilisateur 

class UtilisateursForm (forms.ModelForm): 
    class Meta: 
        model = Utilisateurs 
        fields = "__all__"