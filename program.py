# Journal Prompt Program
# Author: Callum Morich
# Coptyright 2025 Callum Morich

import random

file = open("prompts.txt", "r") # Need to add encoding
prompt_list = file.readlines()
file.close()

list_len = len(prompt_list) - 1

prompt_num = random.randint(0, list_len)
prompt = prompt_list[prompt_num]

# print(prompt_list[prompt_num])
user_response = input(prompt)

file = open("responses.txt", "a")
file.write(prompt + "\n" + user_response + "\n\n") # This works, but writes to the final character

file.close()