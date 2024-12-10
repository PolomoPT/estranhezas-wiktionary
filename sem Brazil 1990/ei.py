import re

input_file_path = 'acentos\sem Brazil 1990\lemmas.txt'
output_file_path = 'acentos\sem Brazil 1990\com_éi_etc.txt'

with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        match_ü = re.search('éi', line)
        if match_ü:
            output_file.write("|"+line)