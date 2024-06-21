from src.data_collection import *
from src.data_collection import *
from src.data_preprocess import *
from src.chatbot_prompt_template import *

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI

from pprint import pprint

#La question qu'on pose au chat bot
## à modifier pour tester
question="Que c'est t'il passé récemment à propos de la France ?"




#récupère 20 articles de l'API de Guardian et le stocke dans un fichier (articles.json)
data = get_guardian_articles_data("", pagesize=100)

documents = load_json_bodies_in_Document_list()
documents = split_data(documents)

#Création de la base de donnée vectorielle "Chroma"
#Nom de la base de données "articles"
#Sauvegarde la database au chemin 'database/chroma/'
#Utilise une fonction embedding par "défault", OpenAIEmbeddings()
articles_chroma_db = Chroma(
    "articles",
    persist_directory='database/chroma/',
    embedding_function=OpenAIEmbeddings(),
)


#Ajout des documents à la base de donnée
articles_chroma_db = articles_chroma_db.from_documents(documents, OpenAIEmbeddings())


#Compare la question avec les articles stockés pour trouver les 4 plus proches
'''docs = articles_chroma_db.similarity_search(question)

for doc in docs:
    print(doc.page_content)
    print (doc.metadata)'''

#récupère la variable d'environnement OPENAI_API_KEY pour accéder à openai
os.getenv('OPENAI_API_KEY')
chat_model = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)

#récupération du template (voir chatbot_prompt_template.py)
chatbot_prompt_template = chatbot_prompt_template()

#chaine de données utilisée pour la requête à chat-gpt
##"context" et "question" --> récupère k article dans la base de données ayant un rapport avec la question donnée
##chatbot_prompt_template --> template pour la requête (voir chatbot_prompt_template.py)
##chat_model --> le modèle de chat-gpt utilisé
##StrOutputParser() --> envoie en réponse un string
chatbot_chain = (
    {"context": articles_chroma_db.as_retriever(k=4), "question": RunnablePassthrough()}
    | chatbot_prompt_template
    | chat_model
    | StrOutputParser()
)

#envoie de la chaine de données à chatgpt afin de récupérer une réponse
chatbot_response = chatbot_chain.invoke(question)

print(chatbot_response)