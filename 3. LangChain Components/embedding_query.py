from langchain_google_genai import GoogleGenerativeAIEmbeddings

from dotenv import load_dotenv
load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-2", dimensions=20)

koi_simple_string = "A sample string"

result = embeddings.embed_query(koi_simple_string)

print(result)  