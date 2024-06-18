from src.data_collection import *
from src.data_collection import *
from src.data_preprocess import *

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

from pprint import pprint

#récupère 20 articles de l'API de Guardian et le stocke dans un fichier (articles.json)
data = get_guardian_articles_data("", pagesize=20)


documents = load_json_bodies_in_Document_list()
documents = split_data(documents)
pprint(documents)

#Création de la base de donnée vectorielle "Chroma"
#Nom de la base de données "articles"
#Sauvegarde la database au chemin 'database/chroma/'
#Utilise une fonction embedding par "défault", OpenAIEmbeddings()
reviews_vector_db = Chroma(
    "articles",
    persist_directory='database/chroma/',
    embedding_function=OpenAIEmbeddings(),
)


#Ajout des documents à la base de donnée
db = reviews_vector_db.from_documents(documents, OpenAIEmbeddings())



question="What happen about space ?"

#Compare la question avec les articles stockés pour trouver les 4 plus proches
docs = db.similarity_search(question)

for doc in docs:
    print(doc.page_content)
    print (doc.metadata)


