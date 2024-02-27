import os
import time
import random
from termcolor import colored


class Quiz:
    def __init__(self, BASE_DIR: str,) -> None:

        self.BASE_DIR = BASE_DIR
        self.all_questions = {}
        self.dict_for_one_questio = {}
        self.anwsers = []
        self.options = []
        self.all_wrongs = 0
        self.all_correct = 0
        self.correct = 0

    # load questions from folder questions in rot dir
    def load_questions(self,):

        load_questions = os.listdir(self.BASE_DIR)
        random.shuffle(load_questions)  # mix list
        random.shuffle(load_questions)  # mix list

        for number, question in enumerate(load_questions, start=1):
            with open(f"questions/{question}", "r") as file:
                self.dict_for_one_questio.clear()
                self.anwsers.clear()
                self.options.clear()
                for line_number, line in enumerate(file, start=1):
                    match line_number:
                        case 1:
                            for possition, character in enumerate(line, start=1):
                                if character == "x":
                                    self.anwsers.append(possition)

                            self.dict_for_one_questio["anwsers"] = self.anwsers.copy(
                            )
                        case 2:
                            self.dict_for_one_questio["question"] = line
                        case _:
                            self.options.append(line)
                    self.dict_for_one_questio['options'] = self.options.copy()
            self.all_questions[f"#{number}"] = self.dict_for_one_questio.copy()


# start quiz

    def run_quiz(self,):

        os.system('cls' if os.name == 'nt' else "clear")
        print(colored("Welcom, This is help for u!!!", 'light_magenta'))
        for key, value in self.all_questions.items():
            self.correct = 0
            print(
                colored(f"{(len(self.all_questions[key]['question'])+16)*'-'}", 'yellow'))
            print(
                colored(f"Question ({key}): {value['question'][:-1]}", 'blue'))
            print(
                colored(f"{(len(self.all_questions[key]['question'])+16)*'-'}", 'yellow'))
            for i in range(len(value['options'])):
                print(colored(f"{i+1}){value['options'][i][:-1]}"))

            while (True):
                try:

                    user_input = self.user_input()
                    for possition in set(user_input):
                        if int(possition) in value['anwsers']:
                            self.correct += 1
                    break

                except ValueError:
                    print("Ohhh,pleas input numbers from 1 to 9")

            if self.correct == len(value['anwsers']):
                print(colored("Correct", "green"))
                self.all_correct += 1
            else:
                print(colored("Mistake", "light_red"))
                self.all_wrongs += 1

        os.system('cls' if os.name == 'nt' else 'clear')

    def user_input(self,) -> str:
        user_input = input(colored("your anwser is: ", "cyan"))

        return user_input

    def print_stat(self,) -> None:
        os.system('cls' if os.name == 'nt' else "clear")
        print(colored("-------------------------------", "magenta"))
        print(colored(f"All questions: {len(self.all_questions)}", "yellow"))
        print(colored(f"Correct: {self.all_correct}", "green"))
        print(colored(f"Wrong: {self.all_wrongs}", "light_red"))
        print(colored("-------------------------------", "magenta"))

    def comapre_anwser(self,):
        pass
