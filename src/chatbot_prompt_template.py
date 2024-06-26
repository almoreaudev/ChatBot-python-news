
from langchain.prompts import (
    PromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
)
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough


def chatbot_prompt_template():

    #Le template système du prompt posé à chat-gpt.
    #Il reçoit les informations contextuel gràce à "context"
    systeme_template_str = """Your job is to give summary of recent news to the user. 
    For this I give you various recent article from the journal Guardian.
    Write a summary of each article.
    Only use information that I give you, don't create ungiven information.
    {context}
    """

    #Chatgpt reçoit d'abord un message "système" ayant le prompt et le contexte
    system_prompt = SystemMessagePromptTemplate(
        prompt=PromptTemplate(
            input_variables=["context"], template=systeme_template_str
        )
    )

    #Ensuite, il reçoit un message "humain" qui contient la question posé par l'humain
    human_prompt = HumanMessagePromptTemplate(
        prompt=PromptTemplate(input_variables=["question"], template="{question}")
    )
    messages = [system_prompt, human_prompt]

    chatbot_prompt_template = ChatPromptTemplate(
        input_variables=["context", "question"], messages=messages
    )

    return chatbot_prompt_template