# Journal Prompt Program
# Author: Callum Morich
# Coptyright 2025 Callum Morich

import random
from datetime import datetime

with open("prompts.txt", "r", encoding="utf-8") as file:
    prompt_list = file.readlines()

prompt = random.choice(prompt_list)
user_response = input(prompt)

with open("responses.txt", "a", encoding="utf-8") as file:
    timestamp = datetime.now().strftime("%a %d-%m-%y, %I:%M%p")
    file.write(timestamp + "\n" + prompt + "\n" + user_response + "\n==========\n")