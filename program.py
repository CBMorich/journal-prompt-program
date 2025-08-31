# Journal Prompt Program
# Author: Callum Morich
# Coptyright 2025 Callum Morich

import random
import datetime

with open("prompts.txt", "r", encoding="utf-8") as file:
    prompt_list = file.readlines()

prompt = random.choice(prompt_list)
user_response = input(prompt)

with open("responses.txt", "a", encoding="utf-8") as file:
    file.write(prompt + "\n" + user_response + "\n\n")