class QuizBrain:

    def __init__(self,q_list):
        self.que_no = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.que_no < len(self.question_list)


    def next_que(self):
        cur_que = self.question_list[self.que_no]
        self.que_no += 1
        user_ans = input(f"Q.{self.que_no}: {cur_que.text} (True/False): ")
        self.check_ans(user_ans,cur_que.answer)

    def check_ans(self,user_ans,correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("You got it right!!!")
            self.score += 1
        else:
            print("That's Wrong.....")

        print(f"The correct answer is {correct_ans}.")
        print(f"Your current score: {self.score} / {self.que_no}")
        print("\n")
