from dotenv import load_dotenv
import os
import requests
import json
from utils.util_decorator import save_to_json

#Charge les variables d'environnement du fichier .env
load_dotenv()

guardian_api_key = os.getenv("GUARDIAN_API_KEY")

'''
Fonction : get_guardian_articles(...)

@save_to_json('database/output.json') --> décorateur permettant de sauvegarder le résultat dans un fichier json
voir utils/util_decorator.py

Arguments :
query --> sur quoi se base la recherche pour l'API (rien "", "technology", "football", etc)
api_key --> prends la varible d'environnement "GUARDIAN_API_KEY" par défault
page et pagesize --> Le numéro de la page avec le nombre d'article pour la page

Retour :
Liste multi-dimensionnel JSON contenant la réponse de l'API
'''
@save_to_json('data/articles.json')
def get_guardian_articles_data(query, api_key=guardian_api_key, page=1, pagesize=10, orderBy='newest') -> json:
    #configuration de la requête (url et params)
    url = f"https://content.guardianapis.com/search"
    params = {
        'api-key': api_key,
        'q': query,
        'order-by': orderBy,
        'page': page,
        'page-size': pagesize,
        'show-fields': 'headline,body'
    }

    #requête et sauvegarde dans une variable de la réponse
    response = requests.get(url, params=params)
    #vérification du bon déroulement de la requête (code 200)
    if response.status_code == 200:
        #retour de la variable response au format json
        return response.json()
    else:
        raise Exception(f"Failed get data: {response.status_code}")