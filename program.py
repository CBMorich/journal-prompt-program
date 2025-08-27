# Journal Prompt Program
# Author: Callum Morich
# Coptyright 2025 Callum Morich

file = open("prompts.txt", "r") # Need to add encoding
prompt_list = file.readlines()
file.close()

list_len = len(prompt_list)

print(list_len)
print(prompt_list)
