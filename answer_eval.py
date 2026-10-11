import requests
import json

class AnswerEvaluator:
  def __init__(self, model= "llama3.2"):
    self.model = model
    self.url = "http://localhost:11434/api/generate"

  def evaluate(self, question, answer):

        prompt = f"""
You are an expert technical interviewer evaluating a candidate's answer.

Question:
{question}

Candidate Answer:
{answer}

Evaluate the candidate's answer.

Return ONLY valid JSON using exactly this structure:

{{
    "score": 0,
    "correct": false,
    "concept_coverage": 0.0,
    "missing_concepts": [],
    "misconceptions": [],
    "feedback": ""
}}

Rules:

1. Score the answer from 0 to 10.
2. "correct" should be true only if the answer is substantially correct.
3. "concept_coverage" must be a value between 0.0 and 1.0.
4. Identify important concepts missing from the answer.
5. Identify factual misconceptions if present.
6. Give concise constructive feedback.
7. Do not evaluate grammar unless it affects technical meaning.
8. Do not assume information that is not present in the answer.
9. Return only JSON.
"""

        data = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "format": "json",
            "options": {
                "temperature": 0.1
            }
        }

        response = requests.post(self.url, json=data)

        response.raise_for_status()

        result = response.json()

        return json.loads(result["response"])