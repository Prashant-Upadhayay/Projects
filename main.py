from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below.

Here is the Coversation history.{context}

Question: {question}
Answer:
"""
model = OllamaLLM(model = "llama3")

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print("Hello there, I am an AI chatbot customised for offline chats ,   How can I help you today? or type 'exit' to end the conversation")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        result = chain.invoke({"context": context, "question": user_input})
        print("Bot: ",result)
        context+= f"\nUser:{user_input}\nAI:{result}"
if __name__=="__main__":
    handle_conversation()