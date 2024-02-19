import os
import time
import random

def help():

    print("You should enter only one value, if  u think it will be multiply options simple write \"123\"")
def main():
  
    all_files=os.listdir("questions")
    random.shuffle(all_files)
    wrong_anwser=0
    coorect_anwser=0
    for filename in all_files:
            with open(f"questions\{filename}",'r') as file:
        
                line_number=1
                anwser_is=[]
                for line in file:
                    match line_number:
                        case 1:
                            anwser_index=0
                            for anwser_char in line:
                                if anwser_char == 'x':
                                    anwser_is.append(anwser_index+1)
                                anwser_index+=1
                            line_number+=1
                        case 2:
                        
                            print(f"{(len(line)+11)*'-'}")
                            print(f"|Question: {line[:-1]}|")     
                            print(f"{(len(line)+11)*'-'}")
                        
                            line_number+=1
                        
                        case _:
                            print(f"{line_number-2}){line}")
                            line_number+=1
                
                user_anwser=input("Your anwser is: ")
                coorect=0
                for position in set(user_anwser):
                    
                    if int(position) in anwser_is:
                        coorect+=1 
                    else:
                        coorect-=1
            
                if len(anwser_is) == coorect:
                    print("Congrats, you are rigth\n\n\n")
                    coorect_anwser+=1
                else:
                    print("You have mistake\n\n\n")
                    wrong_anwser+=1
                time.sleep(0.5)

    print(f"All questions: {len(all_files)},\nCorret: {coorect_anwser},\nWrong: {wrong_anwser}.")

if __name__ == "__main__":
    help()
    main()