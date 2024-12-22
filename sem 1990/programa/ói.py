import re

input_file_path = 'sem 1990\\lista.txt'
output_file_path = 'sem 1990\\com_ói.txt'

with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        match = re.search('ói(?=.)(?! )(?!-)(?!s )(?!s-)(?!s$)(?!deo)(?!dea)(?!er)', line)
        if match:
            output_file.write("|"+line)