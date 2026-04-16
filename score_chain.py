from langchain_core.output_parsers import StrOutputParser
from chains.llm import llm
from prompts.score_prompt import score_prompt

score_chain = score_prompt | llm | StrOutputParser()