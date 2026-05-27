# from langchain_openai import OpenAIEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

from dotenv import load_dotenv
load_dotenv()

# embeddings = OpenAIEmbeddings(model="text-embeddings-3")
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-2", output_dimensionality=5)

documents = [
    "Gardening is the rewarding practice of cultivating and tending to plants, flowers, and vegetables, which allows individuals to connect deeply with nature while beautifying their living spaces and producing fresh, organic food.",
    "Photography is the artistic hobby of capturing light with a camera to document meaningful moments, tell compelling visual stories, and express personal creativity through unique angles, lighting, and composition.",
    "Cooking is the versatile culinary art of preparing food by combining ingredients and applying heat, enabling people to explore diverse cultures through different flavors, textures, and traditional recipes.",
    "Reading is a deeply immersive pastime that involves interpreting written language to explore fictional worlds, learn about historical events, and gain new perspectives that broaden one's intellect and imagination.",
    "Hiking is the outdoor activity of walking long distances along scenic trails, forests, or mountains, providing a fantastic way to improve physical fitness while enjoying fresh air and breathtaking natural landscapes."
]

query = "Tell me something about Hiking."

query_embeddings = embeddings.embed_query(query)                            # 1D: [elem1, elem2, ...]
# doc_embedding = embeddings.embed_documents(documents)
doc_embeddings  = [embeddings.embed_query(doc) for doc in documents]        # 2D: [[], [], ...]

scores = cosine_similarity([query_embeddings], doc_embeddings)[0]

scores_with_indexes = list(enumerate(scores))

index, score = sorted(scores_with_indexes, key=lambda x:x[1])[-1]

print("Output:", documents[index])
print("Similarity Score:", score)