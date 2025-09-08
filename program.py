# Journal Prompt Program
# Author: Callum Morich
# Coptyright 2025 Callum Morich

import random
from datetime import datetime

with open("prompts.txt", "r", encoding="utf-8") as file:
    prompt_list = file.readlines()

run_program = True

while run_program == True:
    print("<x> to close program")
    print("<j> to recieve prompt")
    user_response = input(">>>")
    if user_response == "x":
        print("Program Closed")
        run_program = False
    elif user_response == "j":
        prompt = random.choice(prompt_list)
        user_response = input(prompt)
        with open("responses.txt", "a", encoding="utf-8") as file:
            timestamp = datetime.now().strftime("%a %d-%m-%y, %I:%M%p")
            file.write(timestamp + "\n" + prompt + "\n" + user_response + "\n==========\n")
    else:
        print("I didn't understand, please try again")

