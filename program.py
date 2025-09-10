# Journal Prompt Program
# Author: Callum Morich
# Coptyright 2025 Callum Morich

import random
from datetime import datetime

with open("prompts.txt", "r", encoding="utf-8") as file:
    prompt_list = file.readlines()

def prompt_user():
    print("Please select what you would like to do:")
    print("<j> to journal from a prompt")
    print("<x> to exit")
    response = input(">").strip().lower()
    return response

def write_response(prompt, response):
    with open("responses.txt", "a", encoding="utf-8") as file:
        timestamp = datetime.now().strftime("%a %d-%m-%y, %I:%M%p")
        file.write(timestamp + "\n" + prompt + "\n" + response + "\n==========\n")

run_program = True

while run_program == True:
    user_response = prompt_user()
    if user_response == "x":
        print("Program Closed")
        run_program = False
    elif user_response == "j":
        prompt = random.choice(prompt_list)
        response = input(prompt)
        write_response(prompt, response)
    else:
        print("I didn't understand, please try again")

