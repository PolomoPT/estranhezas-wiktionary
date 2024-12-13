import re

input_file_path = 'sem 1945\\lista.txt'
output_file_path = 'sem 1945\\com_mente.txt'

with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        match = re.search('[á|é|í|ó|ú].*mente', line)
        if match:
            output_file.write("|"+line)