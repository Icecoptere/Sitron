from django.http import HttpResponse
from django.shortcuts import render


def home(request, argument=""):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return HttpResponse(f"""
        <h1>Bienvenue {argument} sur mon blog !</h1>
        <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>
    """)
