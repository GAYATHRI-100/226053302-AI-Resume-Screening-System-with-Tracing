from langchain_core.prompts import PromptTemplate

score_prompt = PromptTemplate(
    input_variables=["match_data"],
    template="""
Assign a score between 0 and 100.

Return ONLY JSON:
{{
    "score": 0
}}

Match Data:
{match_data}
"""
)