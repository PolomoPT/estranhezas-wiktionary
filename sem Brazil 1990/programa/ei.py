import re

input_file_path = 'sem Brazil 1990\\lista.txt'
output_file_path = 'sem Brazil 1990\\com_éi_etc.txt'

with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        match = re.search('éi(?=.)(?! )(?!-)(?!s )(?!s-)(?!s$)(?!deo)(?!er)', line)
        if match:
            output_file.write("|"+line)