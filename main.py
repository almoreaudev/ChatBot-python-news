from src.interface_st import *
from src.chatbot_prompt_template import *

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
import os

articles_chroma_db = Chroma(
    collection_name="articles",
    persist_directory='database/chroma/',
    embedding_function=OpenAIEmbeddings()
)

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
    {"context": articles_chroma_db.as_retriever(k=3), "question": RunnablePassthrough()}
    | chatbot_prompt_template
    | chat_model
    | StrOutputParser()
)

#Créé l'interface du chatbot
create_chatbot_interface(chatbot_chain=chatbot_chain)

# Affiche le chat
for chat in st.session_state.history:
    st.write(f"Vous : {chat['user']}")
    st.write(f"NewsBot : {chat['bot']}")