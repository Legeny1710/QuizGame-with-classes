from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    text = i["text"]
    answer = i["answer"]
    new_q = Question(text, answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()

quiz.return_results()