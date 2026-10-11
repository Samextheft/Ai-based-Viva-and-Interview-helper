import requests
import json


class QuestionGenerator:

    def __init__(self, model="llama3.2"):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def generate_question(
        self,
        domain,
        topic,
        difficulty,
        question_type,
        context=None
    ):

        context_text = ""

        if context:
            context_text = f"""
Previous Interaction:

Previous Question:
{context.get("previous_question", "")}

Candidate Answer:
{context.get("candidate_answer", "")}

Missing Concepts:
{context.get("missing_concepts", [])}

Misconceptions:
{context.get("misconceptions", [])}

Adaptive Action:
{context.get("action", "")}
"""

        prompt = f"""
You are a technical interviewer conducting a placement interview.

Generate exactly ONE technical interview question.

Candidate configuration:

Domain: {domain}
Topic: {topic}
Difficulty: {difficulty}
Question Type: {question_type}

{context_text}

Use the adaptive action to determine what kind of question should be generated.

Rules for adaptive actions:

- follow_up:
  Ask a question that explores the candidate's incomplete understanding.

- counter:
  Ask a question that challenges or tests the misconception identified
  in the previous answer.

- increase_difficulty:
  Ask a more challenging question related to the same topic.

- decrease_difficulty:
  Ask an easier question that checks the fundamental concept.

Return ONLY valid JSON.

Use exactly this structure:

{{
    "question": "string",
    "domain": "string",
    "topic": "string",
    "difficulty": "string",
    "question_type": "string"
}}

Additional rules:

1. Generate exactly ONE question.
2. Do not provide the answer.
3. Do not provide an explanation.
4. Keep the question relevant to the selected topic.
5. Do not add extra JSON fields.
6. Do not use Markdown.
7. Return only JSON.
"""

        data = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "format": "json",
            "options": {
                "temperature": 0.2
            }
        }

        response = requests.post(
            self.url,
            json=data
        )

        response.raise_for_status()

        result = response.json()

        return json.loads(result["response"])