import re

input_file_path = 'sem 1945\\lista.txt'
output_file_path = 'sem 1945\\com_ü_etc.txt'

with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        match_ï = re.search('ï', line)
        match_ü = re.search('(?<=[q|g|a|â|á|à|e|ê|é|è|i|í|ì|o|ô|ó|ò])ü', line) #antecedido por <q> <g> ou vogal
        if match_ï or match_ü:
            output_file.write("|"+line)