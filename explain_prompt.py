from langchain_core.prompts import PromptTemplate

explain_prompt = PromptTemplate(
    input_variables=["score", "match_data"],
    template="""
Explain why this score was given.

Keep it clear and factual.

Match Data:
{match_data}

Score:
{score}
"""
)