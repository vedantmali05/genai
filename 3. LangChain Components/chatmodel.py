from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0, max_output_tokens=1000)

result = model.invoke("Write something about India in 20 words max.")

print(result)