import json
from chains.extract_chain import extract_chain
from chains.match_chain import match_chain
from chains.score_chain import score_chain
from chains.explain_chain import explain_chain


def safe_parse(text):
    try:
        return json.loads(text)
    except:
        return {"error": "Invalid JSON", "raw_output": text}


def run_pipeline(resume, job):

    print("\n--- Pipeline Started ---")

    # Step 1: Extract
    extracted_raw = extract_chain.invoke({"resume": resume})
    extracted = safe_parse(extracted_raw)

    # Step 2: Match
    matched_raw = match_chain.invoke({
        "resume_data": extracted,
        "job_description": job
    })
    matched = safe_parse(matched_raw)

    # Step 3: Score
    score_raw = score_chain.invoke({
        "match_data": matched
    })
    score = safe_parse(score_raw)

    # Step 4: Explanation
    explanation = explain_chain.invoke({
        "score": score,
        "match_data": matched
    })

    return {
        "extracted": extracted,
        "matched": matched,
        "score": score,
        "explanation": explanation
    }


if __name__ == "__main__":

    with open("data/job_description.txt") as f:
        job = f.read()

    resumes = [
        ("Strong", open("data/resume_strong.txt").read()),
        ("Average", open("data/resume_avg.txt").read()),
        ("Weak", open("data/resume_weak.txt").read())
    ]

    for label, resume in resumes:
        print(f"\n===== {label} Candidate =====")

        result = run_pipeline(resume, job)

        print(json.dumps(result, indent=2))