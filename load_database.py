from src.data_collection import *
from src.data_collection import *
from src.data_preprocess import *
from src.interface_st import *
from src.chatbot_prompt_template import *

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI


#récupère 20 articles de l'API de Guardian et le stocke dans un fichier (articles.json)
get_guardian_articles_data("", pagesize=100)

documents = load_json_bodies_in_Document_list()
documents = split_data(documents)

#Création de la base de donnée vectorielle "Chroma"
#Nom de la base de données "articles"
#Créer la database à partir des "documents"
#Sauvegarde la database au chemin 'database/chroma/'
#Utilise une fonction embedding par "défault", OpenAIEmbeddings()
articles_chroma_db = Chroma.from_documents(
    collection_name="articles",
    documents=documents,
    persist_directory='database/chroma/',
    embedding=OpenAIEmbeddings()
)
