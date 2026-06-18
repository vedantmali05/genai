import json
from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_google_genai import ChatGoogleGenerativeAI

# STEP 1: Load Environment Variables
load_dotenv()

# STEP 2: Load and Inspect the Document

loader = TextLoader("./cricket.txt", encoding='utf-8')
docs = loader.load()
doc = docs[0]

print(f"📄 Document Type: {type(doc).__name__}")
print(f"⚙️  Metadata: {json.dumps(doc.metadata, indent=2)}")
print(f"📏 Content Length: {len(doc.page_content)} characters")
print("-" * 60)
print("📝 Content:")
print("-" * 60)
print(doc.page_content)
print("-" * 60)

# STEP 3: Create Prompt Template & Output Parser

prompt = PromptTemplate(
    template="Please generate me a summary of {topic}, strictly in 50 words.",
    input_variables=["topic"]
)
parser = StrOutputParser()

# STEP 4: Initialize the Chat Model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# STEP 5: Construct and Invoke the Chain
chain = prompt | model | parser
result = chain.invoke({'topic': doc.page_content})

print(result)