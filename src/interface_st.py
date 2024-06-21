import streamlit as st


def create_chatbot_interface(chatbot_chain):

    st.title("News bot")
    st.write("Bonjour je suis News bot ! \nDemande moi des nouvelles du jour et je te ferais un résumé d'articles de journaux venant de The Guardian.")

    # Initialise l'historique
    if 'history' not in st.session_state:
        st.session_state.history = []

    # Texte input pour que l'utilisateur puisse entrer du texte 
    user_input = st.text_input("Vous", key="user_input")

    # Si user_input est utilisé (si l'utilisateur entre un texte et appuie sur entrée)
    if user_input:
        # envoie de la chaine de données à chatgpt afin de récupérer une réponse
        chatbot_response = chatbot_chain.invoke(user_input)

        # Met à jour l'historique du chat
        st.session_state.history.append({"user": user_input, "bot": chatbot_response})

        # Clear the input box
        #st.session_state.user_input = ""
