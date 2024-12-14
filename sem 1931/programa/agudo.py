import re

input_file_path = 'sem 1931\\lista.txt'
output_file_path = 'sem 1931\\oxitonas.txt'

with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        match_final = re.search('(?<![a|e|ei|o|u])(í|ú|ís|ús)$', line)
        match_meio = re.search('(?<![a|e|ei|o|u])(í|ú|ís|ús)( |-)', line)
        if match_final or match_meio:
            output_file.write("|"+line)