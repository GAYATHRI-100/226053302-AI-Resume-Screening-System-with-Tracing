from langchain_core.prompts import PromptTemplate

extract_prompt = PromptTemplate(
    input_variables=["resume"],
    template="""
Extract ONLY explicitly mentioned:

- Skills
- Tools
- Experience

STRICT RULES:
- Do NOT assume anything
- Do NOT add extra text

Return ONLY JSON:
{{
    "skills": [],
    "tools": [],
    "experience": ""
}}

Resume:
{resume}
"""
)