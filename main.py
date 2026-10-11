# from question_gen import QuestionGenerator

# generator  = QuestionGenerator()

# question = generator.generate_question(
#   domain="DBMS",
#   topic="Normalization",
#   difficulty="Beginner",
#   question_type="Scenario_based"
# )

# print ("\nGenerated question:")
# # print(question)
# # print(type(question))
# print(question["question"])

# print("\n Metadata")
# print("Domain:", question["domain"])
# print("Topic:", question["topic"])
# print("Difficulty:", question["difficulty"])
# print("Question_type:", question["question_type"])


# from answer_eval import AnswerEvaluator

# evaluator = AnswerEvaluator()

# question = "What is normalization in DBMS?"

# answer = """
# Normalization is the process of increasing the number of
# duplicate records in a database to improve performance.
# """

# evaluation = evaluator.evaluate(question, answer)

# print("\nEvaluation:")
# print(evaluation)
# from adaptive_control import AdaptiveController


# controller = AdaptiveController()


# evaluation = {
#     "score": 9,
#     "correct": True,
#     "concept_coverage": 0.9,
#     "missing_concepts": [],
#     "misconceptions": [],
#     "feedback": "Excellent understanding."
# }


# decision = controller.decide(evaluation)

# print(decision)



#                                            #
# from question_gen import QuestionGenerator
# from answer_eval import AnswerEvaluator
# from adaptive_control import AdaptiveController


# # Create our components
# generator = QuestionGenerator()
# evaluator = AnswerEvaluator()
# controller = AdaptiveController()


# # --------------------------------
# # Step 1: Generate question
# # --------------------------------

# question_data = generator.generate_question(
#     domain="DBMS",
#     topic="Normalization",
#     difficulty="Intermediate",
#     question_type="Conceptual"
# )

# question = question_data["question"]

# print("\n==============================")
# print("        TECHNICAL VIVA")
# print("==============================")

# print("\nQuestion:")
# print(question)


# # --------------------------------
# # Step 2: Get candidate answer
# # --------------------------------

# answer = input("\nYour Answer:\n")


# # --------------------------------
# # Step 3: Evaluate answer
# # --------------------------------

# evaluation = evaluator.evaluate(
#     question,
#     answer
# )

# print("\n==============================")
# print("         EVALUATION")
# print("==============================")

# print("Score:", evaluation["score"])
# print("Correct:", evaluation["correct"])
# print("Concept Coverage:", evaluation["concept_coverage"])

# print("Missing Concepts:")
# for concept in evaluation["missing_concepts"]:
#     print("-", concept)

# print("Misconceptions:")
# for misconception in evaluation["misconceptions"]:
#     print("-", misconception)

# print("Feedback:")
# print(evaluation["feedback"])


# # --------------------------------
# # Step 4: Adaptive decision
# # --------------------------------

# decision = controller.decide(evaluation)

# print("\n==============================")
# print("      ADAPTIVE DECISION")
# print("==============================")

# print("Action:", decision["action"])
# print("Reason:", decision["reason"])




# from question_gen import QuestionGenerator

# generator = QuestionGenerator()


# context = {
#     "previous_question":
#         "What is normalization in DBMS?",

#     "candidate_answer":
#         "Normalization reduces duplicate data.",

#     "missing_concepts":
#         ["1NF", "2NF", "3NF"],

#     "misconceptions":
#         [],

#     "action":
#         "follow_up"
# }


# question = generator.generate_question(
#     domain="DBMS",
#     topic="Normalization",
#     difficulty="Intermediate",
#     question_type="Conceptual",
#     context=context
# )


# print("\nAdaptive Question:")
# print(question["question"])

# print("\nMetadata:")
# print(question)

from question_gen import QuestionGenerator
from answer_eval import AnswerEvaluator
from adaptive_control import AdaptiveController
from interviewsession import InterviewSession


generator = QuestionGenerator()
evaluator = AnswerEvaluator()
controller = AdaptiveController()


session = InterviewSession(
    domain="DBMS",
    topic="Normalization",
    difficulty="Intermediate",
    question_type="Conceptual"
)


context = None


for i in range(3):

    print("\n================================")
    print(f"          QUESTION {i + 1}")
    print("================================")

    # Generate question
    question_data = generator.generate_question(
        domain=session.domain,
        topic=session.topic,
        difficulty=session.difficulty,
        question_type=session.question_type,
        context=context
    )

    question = question_data["question"]

    print("\nQuestion:")
    print(question)

    # Candidate answer
    answer = input("\nYour Answer:\n")

    # Evaluate
    evaluation = evaluator.evaluate(
        question,
        answer
    )

    print("\nScore:", evaluation["score"])
    print("Coverage:", evaluation["concept_coverage"])
    print("Feedback:", evaluation["feedback"])

    # Adaptive decision
    decision = controller.decide(evaluation)

    print("\nNext Action:", decision["action"])
    print("Reason:", decision["reason"])

    # Store interaction
    session.add_interaction(
        question,
        answer,
        evaluation,
        decision
    )

    # Prepare context for next question
    context = {
        "previous_question": question,
        "candidate_answer": answer,
        "missing_concepts": evaluation["missing_concepts"],
        "misconceptions": evaluation["misconceptions"],
        "action": decision["action"]
    }


print("\n================================")
print("       INTERVIEW COMPLETED")
print("================================")

print("Questions Attempted:",
      session.question_number)