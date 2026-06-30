import json
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_google_genai import ChatGoogleGenerativeAI

# Step 1
load_dotenv()

# Step 2
loader = PyPDFLoader("./genai.pdf")
docs = loader.load()
print(docs)

# Step 3
prompt = PromptTemplate(
    template="Summerize the '{topic}' strictly in 100 words",
    input_variables=['topic']
)
parser = StrOutputParser()

# Step 4
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Step 5
chain = prompt | model | parser
# Extract page content from all document pages to pass as text
context = "\n\n".join(doc.page_content for doc in docs)
result = chain.invoke({'topic': context})

print(result)

"""
Use PyPDFLoader for simple PDFs
Use PDFPlumberLoader for PDFs with tables
Use UnstructuredPDFLoader or AmazonTextractPDFLoader for PDFs with images
Use PyMuPDFLoader for PDFs with layouts or images
"""