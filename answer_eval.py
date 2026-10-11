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


Evaluate the candidate's answer using a consistent technical scoring rubric.

SCORING RUBRIC:
- 0–2: Incorrect, irrelevant, or demonstrates almost no understanding.
- 3–4: Shows limited understanding but contains major omissions
      or significant errors.
- 5–6: Mostly correct understanding but misses important concepts
      or provides insufficient explanation.
- 7–8: Correct and reasonably complete, with minor omissions.
- 9–10: Accurate, complete, and clearly explained, including
        relevant reasoning where appropriate.

EVALUATION RULES:
1. Score only what the candidate actually stated.
2. Do not assume the candidate understands a concept they did not explain.
3. Identify specific missing concepts rather than giving generic criticism.
4. Identify factual misconceptions separately from missing information.
5. Accept technically correct alternative wording and approaches.
6. Do not penalize concise answers when the question requires only
   a concise definition.
7. Make the score, correctness, and feedback consistent with one another.
8. Set concept_coverage between 0.0 and 1.0.
9. Set correct to true only when the answer is substantially correct.
10. Give feedback explaining both what was correct and what needs
    improvement, where applicable.
11. Return only valid JSON matching the requested structure.


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