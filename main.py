from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for qanda in question_data:
    question_text = qanda["question"]
    question_ans = qanda["correct_answer"]
    question = Question(question_text,question_ans)
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_que()

print("You've completed the quiz.")
print(f"Your final score: {quiz.score}/{len(question_bank)}")