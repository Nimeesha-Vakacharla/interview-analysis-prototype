import subprocess

def run_ollama_analysis(stats):

    prompt = f"""
You are an expert AI interview evaluator.

Candidate Data:
{stats}

Evaluate the candidate on:

1. Confidence (0-10)
2. Nervousness (0-10)
3. Presentability (0-10)
4. Confusion (0-10)
5. Eye Contact (0-10)
6. Stability (0-10)
7. Abnormal Behavior (0-10)

Rules:
- Use emotion data + behavior data
- High movement = nervousness
- Low eye contact = poor engagement
- Stable face = confidence
- Inconsistent emotions = confusion

Return STRICT JSON ONLY:

{{
    "scores": {{
        "confidence": 0,
        "nervousness": 0,
        "presentability": 0,
        "confusion": 0,
        "eye_contact": 0,
        "stability": 0,
        "abnormality": 0
    }},
    "reasoning": {{
        "confidence": "",
        "nervousness": "",
        "presentability": "",
        "confusion": "",
        "eye_contact": "",
        "stability": "",
        "abnormality": ""
    }},
    "strengths": [],
    "weaknesses": [],
    "summary": ""
}}
"""

    result = subprocess.run(
        ["ollama", "run", "phi3"],
        input=prompt.encode(),
        stdout=subprocess.PIPE
    )

    output = result.stdout.decode()

    # Clean markdown if model adds it
    return output.replace("```json", "").replace("```", "").strip()