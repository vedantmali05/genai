from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate, load_prompt
import streamlit as st

from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# ################### UI ########################## #

st.set_page_config(layout="wide")
st.header("Research Summarizer Tool")

col1, col2 = st.columns(2, gap="xlarge")

# ################### INPUTS (Left Column) ########################## #

with col1:
    st.subheader("Summarization Settings")
    research_topic = st.selectbox("Select a Research Topic: ", [
        "Deep Learning & Large Language Models",
        "Quantum Computing & Cryptography",
        "CRISPR & Genetic Engineering",
        "Renewable Energy & Climate Solutions",
        "Space Exploration & Exoplanets"
    ])

    output_style = st.selectbox("Choose a style: ", ["ELI5 (Easiest)", "Beginner Level", "Friendly", "Formal", "Technical"], index=2)

    word_count = st.number_input("Enter number of words: ", min_value=25, max_value=1500, value=250)

    elements_to_include = st.multiselect("To Include: ", ["Mathematics", "Analogies", "Example", "Key Takeaways", "Historical Context", "Future Outlook"], default=["Key Takeaways"])

    summarize_clicked = st.button("Summarize", type="primary")


# ################### DYANAMIC PROMPT TEMPLATE ########################## #


prompt = load_prompt("./5. LangChain Prompts/templates.json")

# ################### OUTPUT (Right Column) ########################## #

with col2:
    if summarize_clicked:
        prompt = prompt.invoke({
            'research_topic': research_topic,
            'output_style': output_style,
            'word_count': word_count,
            'elements_to_include': elements_to_include
        })
        
        result = model.invoke(prompt)
        st.write(result.content)