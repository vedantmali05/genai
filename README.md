# GenAI Study and Experimentation Repository

This repository contains structured notebooks, scripts, and examples for learning and experimenting with Generative AI concepts using **LangChain** and **Google Gemini** models.

---

## Repository Structure

The project is organized into modular directories reflecting different stages of LangChain and Generative AI development:

*   **`3. LangChain Components/`**
    *   Basic setups for `ChatGoogleGenerativeAI` (`gemini-2.5-flash`).
    *   Text embeddings and document vector similarity analysis.
*   **`4. LangChain Prompts/`**
    *   `PromptTemplate` generation, inputs, and structure formatting.
    *   Saving and loading prompt configurations (`templates.json`).
    *   Integrating chat history and summarization logic.
*   **`5. Structured Outputs/`**
    *   Extracting raw texts into strictly-typed python objects using `TypedDict` and `Pydantic`.
    *   Using `Annotated` parameters to inject constraints on LLM outputs.
    *   Leveraging `.with_structured_output()` to enforce categorical constraints (via `Literal`).

---

## Setup & Installation

### 1. Clone & Navigate
```bash
git clone git@github.com:vedantmali05/genai.git
cd genai
```

### 2. Environment Setup
Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Keys
Create a `.env` file in the root directory and add your Google API credentials:
```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

---

## Development Guidelines

Refer to `_rules-for-ai.txt` for coding agent constraints and behavior specifications when using AI coding assistants in this repository.