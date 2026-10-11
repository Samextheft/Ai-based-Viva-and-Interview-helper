class InterviewSession:

    def __init__(self, domain, topic, difficulty, question_type):
        self.domain = domain
        self.topic = topic
        self.difficulty = difficulty
        self.question_type = question_type

        self.question_number = 0
        self.history = []

    def add_interaction(self, question, answer, evaluation, decision):

        interaction = {
            "question": question,
            "answer": answer,
            "evaluation": evaluation,
            "decision": decision
        }

        self.history.append(interaction)

        self.question_number += 1

    def get_last_interaction(self):

        if not self.history:
            return None

        return self.history[-1]

    def get_summary(self):

        return {
            "domain": self.domain,
            "topic": self.topic,
            "questions_attempted": self.question_number,
            "history": self.history
        }