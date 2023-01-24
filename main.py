"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Ivana Gulasova
email: ivana.gulasova3@gmail.com
discord: IvanaG #9103
"""
import random
import time

greet = "Hi there!"
section = "-" * 47
text =  """I've generated a random 4 digit number for you.\nLet's play a bulls and cows game."""
list_of_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
game_run = True
play = True
text_enter_a_num = "Enter a number:\n" + section 

def bulls(list1, list2):
        bulls = 0
        for i in range(0, len(list1)):
            if list1[i] == list2[i]:
                bulls += 1
        return bulls

def cows(list1, list2):
    cows = 0
    for index, item in enumerate(list1):
        if item in list2:
            if list1[index] != list2[index]:
                cows += 1
    return cows

def convert_list(list):
    new_list = []
    for str in range(0, len(list)):
        new_list.append(int(list[str]))
    return new_list

def convert(seconds):
    return time.strftime("%H:%M:%S", time.gmtime(seconds))

def conclusion(sec):
    if sec <= 60:
        print("That was amazing!")
    elif sec <= 120:
        print("That was average.")
    else:
        print("That was not so good..")


print("\n" + greet)
print(section)
print(text)
print(section)
print(text_enter_a_num)

while game_run:
    startTime = time.time()
    trials = 0
    while True:
        pc_rand = random.sample(list_of_num, 4)
        if pc_rand[0] == 0:
            random.sample(list_of_num, 4)
        else:
            break
    # print(pc_rand)
    
    while play:
        list_of_guess = []
        guess = input(">>> ")
        for str in guess:
            list_of_guess.append(str)

        while len(list_of_guess) != 4 or list_of_guess[0] == "0" or not all(i.isdigit() for i in list_of_guess) or len(list_of_guess) != len(set(list_of_guess)): 
            if not all(i.isdigit() for i in list_of_guess):
                print("Enter only numbers.")
            elif list_of_guess[0] == "0":  
                print("The numbers can not start with '0'. ")
            elif len(list_of_guess) != 4:
                print("The length of the number is not correct.")
            elif len(list_of_guess) != len(set(list_of_guess)):
                print("Enter numbers without duplicates.")
            
            list_of_guess.clear()
            guess = input(">>> ")
            for str in guess:
                list_of_guess.append(str)

        guess_int_list = convert_list(list_of_guess)
        result_cows = cows(guess_int_list, pc_rand)
        result_bulls = bulls(guess_int_list, pc_rand)

        if result_bulls == 4:
            stopTime = time.time()
            len_of_time = round(stopTime-startTime, 2)
            result_time = convert(len_of_time)
            print("Correct, you've guessed the right number\nin 4 guesses!\n")
            print("The number of trials: ", trials + 1)
            print(f"Total time to guess: {result_time} hod")
            conclusion(len_of_time)
            print(section)
            break
        else:
            bull_word = ""
            if result_bulls == 1:
                bull_word = "bull"
            else:
                bull_word = "bulls"
            cows_word = ""
            if result_cows == 1:
                cows_word = "cow"
            else:
                cows_word = "cows"
            print(f"{result_bulls} {bull_word}, {result_cows} {cows_word}")
            print(section)
            trials += 1

    while True:
        again = input("New game? 'yes' or another sign for 'no' : ")   
        if again == "yes":
            break
        else:
            print("Hope to see you soon, bye")
            quit()
        


    
    




