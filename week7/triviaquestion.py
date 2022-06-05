from tkinter.messagebox import QUESTION
from unicodedata import category


class TriviaQuestion:
    def __init__(self, question, category, difficultylevel, correctanswer, incorrectanswers, id):
        self.question = question
        self.category = category
        self.difficultylevel = difficultylevel
        self.correctanswer = correctanswer
        self.inncorrectanswers = incorrectanswers
        self.id = id

    def __str__(self):
        return f'{self.question} {self.category} {self.difficultylevel} {self.correctanswer}'

    def getQuestion(self):
        return self.question

    def getCategory(self):
        return self.category

    def getDifficultyLevel(self):
        return self.difficultylevel

    def getCorrectAnswer(self):
        return self.correctanswer
    
    def getIncorrectAnswers(self):
        return self.inncorrectanswers

    def getId(self):
        return self.id