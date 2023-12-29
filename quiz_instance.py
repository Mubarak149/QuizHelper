class Quiz:
    def __init__(self):
        self.grade = None
        self.score = 0
        self.answer = []
        self.text_question = ""




    def init_question(self,f,deli):
        text = ""
        with open(f, "r") as txt:
            for i in txt.readlines():
                text += i

            self.text_question = text.split(deli)

    def question_prompt(self,file,deli,options):
        self.init_question(file,deli)
        for ind, q in enumerate(self.text_question[0:5]):
            print(q)
            user = input(f"choose your answer({options}): ")
            self.check_answer(self.answer,user,ind)
        print("you score: ",self.score)
        if self.score/ len(self.text_question[0:5]) == 1:
            self.grade = "A"
        elif self.score/ len(self.text_question[0:5]) >= 0.7:
            self.grade = "B"
        elif self.score/ len(self.text_question[0:5]) >= 0.5:
            self.grade = "C"
        else:
            self.grade = "F"

    def check_answer(self, answer_list, user_answer,n_question):
        if user_answer == answer_list[n_question]:
            self.score += 1
        else:
            return



"""
quiz = Quiz()
quiz.question("quiz_questions.txt")
ans = ["b","b","b","b","c","b","c","b","b","b","b","b","a","c","b","b","c","b","b","a",]
quiz.answer.extend(ans)
print(quiz.answer)
quiz.question_prompt("quiz_questions.txt","]","A-B-C-D") (your question file, what separate question from the file, available option to choose your answer)
print(quiz.grade)
"""
