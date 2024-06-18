#importe les régulars expression pour supprimer les balises HTML
import re
from src.data_collection import *

from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import JSONLoader
from langchain_core.documents import Document

from bs4 import BeautifulSoup

'''
Fonction load_json_body()

Charge le fichier JSON gràce à JSONLoader, un module pour charger les documents JSON pour l'utilisation de langchain
Charge uniquement les balises "body" des résultats du fichier JSON (pas toute l'arborescence)

Retour :
Une liste de "Document", un format spécial de langchain pour ajouter les données à ChromaDB
'''
def load_json_bodies_in_Document_list() -> list[Document]:
    loader = JSONLoader(
    file_path='data/articles.json',
    jq_schema='.response.results[].fields.headline')

    documents = loader.load()
    return documents


'''
Fonction split_data(...)

Argument :
documents --> list de "Document" 

Retour : 
Une liste de documents split et nettoyé des balises HTML 
'''
def split_data (documents):

    #récupère les données au format JSON
    #data = get_guardian_articles_data(query, pagesize=5)     
        
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    documents = text_splitter.split_documents(documents)
    for d in documents:
        d.page_content=BeautifulSoup(d.page_content, "html.parser").get_text()

    return documents
