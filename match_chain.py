from langchain_core.output_parsers import StrOutputParser
from chains.llm import llm
from prompts.match_prompt import match_prompt

match_chain = match_prompt | llm | StrOutputParser()