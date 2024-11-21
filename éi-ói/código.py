import re

input_file_path = 'éi-ói\\lemmas.txt'
output_file_path = 'éi-ói\\com_ei_oi.txt'

with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        match_éi = re.search('(éi|ói)(?=.)(?!s )(?!s$)', line)
        if match_éi:
            output_file.write("|"+line)