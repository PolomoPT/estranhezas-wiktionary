import re

input_file_path = 'ü etc\sem Brazil 1990\lemmas.txt'
output_file_path = 'ü etc\sem Brazil 1990\sem_1990.txt'

with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        match_ü = re.search('[q|g]ü', line)
        if match_ü:
            output_file.write("|"+line)