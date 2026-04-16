from langchain_core.output_parsers import StrOutputParser
from chains.llm import llm
from prompts.explain_prompt import explain_prompt

explain_chain = explain_prompt | llm | StrOutputParser()