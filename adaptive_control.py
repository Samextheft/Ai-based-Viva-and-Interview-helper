class AdaptiveController:

    def decide(self, evaluation):

        score = evaluation["score"]
        coverage = evaluation["concept_coverage"]
        misconceptions = evaluation["misconceptions"]

        # Misconception takes priority
        if misconceptions:
            return {
                "action": "counter",
                "reason": "Misconception detected"
            }

        # Strong performance
        if score >= 8 and coverage >= 0.8:
            return {
                "action": "increase_difficulty",
                "reason": "Strong understanding demonstrated"
            }

        # Partial understanding
        if score >= 5:
            return {
                "action": "follow_up",
                "reason": "Partial understanding detected"
            }

        # Weak performance
        return {
            "action": "decrease_difficulty",
            "reason": "Insufficient understanding demonstrated"
        }