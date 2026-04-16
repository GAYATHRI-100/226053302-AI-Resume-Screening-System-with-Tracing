from langchain_core.output_parsers import StrOutputParser
from chains.llm import llm
from prompts.extract_prompt import extract_prompt

extract_chain = extract_prompt | llm | StrOutputParser()
