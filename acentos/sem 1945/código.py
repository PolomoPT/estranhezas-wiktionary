import re

input_file_path = 'acentos\sem 1945\com_ü_etc.txt'
output_file_path = 'acentos\sem 1945\lemmas.txt'

with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        match_ï = re.search('ï', line)
        match_ü = re.search('ü', line)
        if match_ï or match_ü:
            output_file.write("|"+line)