class QuizBrain:
    def __init__(self, q_list):
        self.q_list = q_list
        self.q_number = 0
        self.score = 0

    def still_has_questions(self):
        return self.q_number < len(self.q_list)


    def next_question(self):
        current_question = self.q_list[self.q_number]
        self.q_number += 1
        user_answer = input(f"Q{self.q_number}: {current_question.text}, True or False?: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right! Well Done!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"The correct answer was {correct_answer}")
        print(f'Your score: {self.score}/{self.q_number}')
        print("\n")

    def return_results(self):
        print("You have completed the Quiz!")
        print(f'Your Final score: {self.score}/{self.q_number}')
