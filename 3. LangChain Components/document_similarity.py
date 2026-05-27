from langchain_google_genai import GoogleGenerativeAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

from dotenv import load_dotenv
load_dotenv()


embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-2", output_dimensionality=20)

documents = [
    "Gardening is the rewarding practice of cultivating and tending to plants, flowers, and vegetables, which allows individuals to connect deeply with nature while beautifying their living spaces and producing fresh, organic food.",
    "Photography is the artistic hobby of capturing light with a camera to document meaningful moments, tell compelling visual stories, and express personal creativity through unique angles, lighting, and composition.",
    "Cooking is the versatile culinary art of preparing food by combining ingredients and applying heat, enabling people to explore diverse cultures through different flavors, textures, and traditional recipes.",
    "Reading is a deeply immersive pastime that involves interpreting written language to explore fictional worlds, learn about historical events, and gain new perspectives that broaden one's intellect and imagination.",
    "Hiking is the outdoor activity of walking long distances along scenic trails, forests, or mountains, providing a fantastic way to improve physical fitness while enjoying fresh air and breathtaking natural landscapes."
]

query = "Tell me something about Cooking."

doc_embeddings = [embeddings.embed_query(doc) for doc in documents]
query_embedding = embeddings.embed_query(query)

similarity_scores = cosine_similarity([query_embedding], doc_embeddings)[0]

similarity_scores_with_index = list(enumerate(similarity_scores))

index, score = sorted(similarity_scores_with_index, key=lambda x:x[1])[-1]

print(documents[index])
print(score)