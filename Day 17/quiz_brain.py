class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"{self.question_number + 1}: {current_question.text}. [True/False]: ")
        self.check_answer(user_answer, current_question.answer)
        self.question_number += 1  # Increment the question number after each question

    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("You got it right!")
        else:
            print("You got it wrong.")
            print(f"The correct answer is {correct_ans}")