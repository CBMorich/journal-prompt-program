# Journal Prompt Program
# Author: Callum Morich
# Coptyright 2025 Callum Morich

import random

file = open("prompts.txt", "r") # Need to add encoding
prompt_list = file.readlines()
file.close()

list_len = len(prompt_list) - 1

prompt_num = random.randint(0, list_len)

print(prompt_list[prompt_num])

