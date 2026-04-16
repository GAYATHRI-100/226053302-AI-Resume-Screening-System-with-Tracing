from langchain_core.prompts import PromptTemplate

match_prompt = PromptTemplate(
    input_variables=["resume_data", "job_description"],
    template="""
Compare resume with job description.

Return ONLY JSON:
{{
    "matched_skills": [],
    "missing_skills": []
}}

Resume Data:
{resume_data}

Job Description:
{job_description}
"""
)