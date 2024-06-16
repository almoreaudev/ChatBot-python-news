#importe les régulars expression pour supprimer les balises HTML
import re
from src.data_collection import get_guardian_articles_data

# Récupère un "article", une multi-liste comportant les informations d'un article 
# rend un dictionnaire avec deux keys 'headline' et 'body'
def preprocess_article(article):
    headline = article['fields']['headline']
    body = article['fields']['body']
    body = re.sub('<[^<]+?>', '', body)
    return {'headline': headline, 'body': body}

'''
Fonction preprocess_articles(...)

Argument :
query --> sur quoi se base la recherche pour l'API (rien "", "technology", "football", etc)

Retour : 
Une liste de dictionnaire ayant deux keys pour chaque élément "headline" et "body"
'''
def preprocess_articles(query=""):
    data = get_guardian_articles_data(query, pagesize=1)
    articles = data['response']['results']       
    
    return [preprocess_article(article) for article in articles]