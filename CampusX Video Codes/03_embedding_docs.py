from langchain_google_genai import GoogleGenerativeAIEmbeddings

from dotenv import load_dotenv
load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-2", dimensions=20)

koi_strings_array = ["Alice", "John", "Jasper", "Casper", "Tabitha"]

result = embeddings.embed_documents(koi_strings_array)

print(result)  