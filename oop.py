import os
import time
import random
from types import prepare_class
from termcolor import colored


class Quiz:
    def __init__(self, BASE_DIR: str,) -> None:

        self.BASE_DIR = BASE_DIR
        self.all_questions = []

    def help(self,):
        print(colored("Welcom, This is help for u!!!", "light_magenta"))

    def load_questions(self,):
        self.all_questions = os.listdir(self.BASE_DIR)
        random.shuffle(self.all_questions)
        random.shuffle(self.all_questions)

    def run_quiz(self,):
        for question in self.all_questions:
            with open(f"questions/{question}", "r") as file:
                for line in file:
                    print(line.index())

    def user_input(self,):
        pass

    def comapre_anwser(self,):
        pass


if __name__ == "__oop__":
    quiz = Quiz()
