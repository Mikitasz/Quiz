import os
import time
import random
from termcolor import colored


def help():

    print(
        colored(
            'You should enter only one value, if  u think it will \
             be multiply options simple write "123"',
            "light_magenta",
        )
    )


def main():
    all_files = os.listdir("questions")
    random.shuffle(all_files)
    random.shuffle(all_files)
    wrong_anwser = 0
    mistakes = []
    anws = []
    coorect_anwser = 0
    quest_number = 1
    for filename in all_files:
        with open(f"questions/{filename}", "r") as file:

            os.system("cls" if os.name == "nt" else "clear")
            line_number = 1
            anwser_is = []
            for line in file:
                match line_number:
                    case 1:
                        anwser_index = 0
                        for anwser_char in line:
                            if anwser_char == "x":
                                anwser_is.append(anwser_index + 1)
                            anwser_index += 1
                        line_number += 1
                    case 2:

                        print(colored(f"{(len(line)+11)*'-'}", "yellow"))
                        print(
                            colored(
                                f"Question (#{quest_number}): {line[:-1]}",
                                "blue",
                            )
                        )
                        print(colored(f"{(len(line)+11)*'-'}", "yellow"))

                        line_number += 1
                        quest_number += 1

                    case _:
                        print(colored(f"{line_number-2}){line}", "white"))
                        line_number += 1

            user_anwser = input(colored("Your anwser is: ", "cyan"))
            coorect = 0
            for position in set(user_anwser):

                if int(position) in anwser_is:
                    coorect += 1
                else:
                    coorect -= 1

            if len(anwser_is) == coorect:
                print(colored("Correct\n\n\n", "green"))
                coorect_anwser += 1
            else:
                print(colored("Mistake\n\n\n", "light_red"))
                wrong_anwser += 1
                anws.append(set(user_anwser))
                mistakes.append(filename)

            time.sleep(0.5)

            os.system("cls" if os.name == "nt" else "clear")

    print(colored("-------------------------------------------", "magenta"))
    print(colored(f"All questions: {len(all_files)}", "yellow"))
    print(colored(f"Corret: {coorect_anwser}", "green"))
    print(colored(f"Wrong: {wrong_anwser}", "light_red"))
    print(colored("-------------------------------------------", "magenta"))

    print(colored("Summury", "blue"))
    for mistake, awnser in zip(mistakes, anws):
        print(colored(f"{mistake} and your anwser is: {awnser}", "red"))


if __name__ == "__main__":
    help()
    main()
