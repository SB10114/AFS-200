class TriviaGame:
    def __init__(self):
        self.questions =[]

    def addQuestion(self, question):
        self.questions.append(question)

    def scoreQuestion(self, answers):
        self.correctanswers = []
        self.incorrectanswers = []
        for index in range(0, len(self.questions)):
            if self.questions[index].correctanswer == answers[index]:
                self.correctanswers.append(self.questions[index])
            else:
                self.incorrectanswers.append(self.questions[index])