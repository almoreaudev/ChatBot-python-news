from src.data_collection import *
from src.data_collection import *
from src.data_preprocess import *
from src.interface_st import *
from src.chatbot_prompt_template import *

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI


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
    {"context": articles_chroma_db.as_retriever(k=4, fetch_k=100), "question": RunnablePassthrough()}
    | chatbot_prompt_template
    | chat_model
    | StrOutputParser()
)

create_chatbot_interface(chatbot_chain=chatbot_chain)

# Affiche le chat
for chat in st.session_state.history:
    st.write(f"Vous : {chat['user']}")
    st.write(f"NewsBot : {chat['bot']}")