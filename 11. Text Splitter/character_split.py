from langchain_text_splitters import CharacterTextSplitter

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("./genai.pdf")
docs = loader.load()

splitter = CharacterTextSplitter(
    separator="",
    chunk_size=102,
    chunk_overlap=20
)

result = splitter.split_documents(docs)

for i, item in enumerate(result):
    print(f"Chunk {i}: {item.page_content}", end="\n\n")