from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
You are an expert research communicator and summarizer. Your goal is to summarize complex scientific and technical topics into highly engaging, readable, and structured explanations.
Please synthesize and explain the following research topic:
Topic: {research_topic}
Adhere strictly to the following parameters for the output:
1. Target Style & Tone:
   You must write this explanation in a "{output_style}" style.
   - If "ELI5 (Easiest)": Explain like I'm 5 years old. Use extremely simple terms, common analogies, and zero jargon.
   - If "Beginner Level": Use basic concepts, simple sentence structures, and explain any unavoidable technical terms simply.
   - If "Friendly": Maintain an encouraging, warm, conversational, and accessible tone.
   - If "Formal": Write as a highly professional academic or analyst, maintaining an authoritative, objective, and precise tone.
   - If "Technical": Write for peers in the field. Do not shy away from advanced terminology, rigorous explanations, and precise mechanisms.
2. Length Constraint:
   The entire explanation should be approximately {word_count} words in length. Do not exceed this limit or shall not fall significantly short of it.
3. Key Elements to Incorporate:
   Ensure that your explanation integrates the following requested elements naturally:
   {elements_to_include}
Structure your response cleanly using markdown headings, lists, or bold text to make it highly scannable and visually appealing.
""",
input_variables=['research_topic', 'output_style', 'word_count', 'elements_to_include']
)

template.save("./5. LangChain Prompts/templates.json")