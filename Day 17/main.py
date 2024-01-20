from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_back = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_back.append(new_question)

quiz = QuizBrain(question_back)

while quiz.still_has_questions():
    quiz.next_question()