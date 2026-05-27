from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

chat_template = ChatPromptTemplate([
    ("system", "You are a helpful AI Assitant. Never reply 'Based on our previous chat' or similar strings ever."), 
])

print("Chat with AI.")
print("Enter \"/bye\" to exit.")

while True:
    user_input = input("You: ")
    chat_template.append(("human", user_input))
    if user_input == "/bye":
        break
    result = model.invoke(chat_template.format_messages()).content
    chat_template.append(("ai", result))
    print("AI: ", result)


print(chat_template)