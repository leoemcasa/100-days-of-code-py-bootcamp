"""Main"""
from question_model import Question
from data import question_data
from quiz_brain import QuizBrains

question_bank = []

for question in question_data:
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)

quiz = QuizBrains(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Terminô. FIM")
print(f"Final score is: {quiz.score}/{quiz.question_number}")