import re

input_file_path = '1911 ou 1943\\lemmas.txt'
output_file_path = '1911 ou 1943\com acento.txt'

with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        match = re.search('â|á|à|ä|ê|é|è|ë|í|ì|ï|ô|ó|ò|ö|ú|ù|ü', line) ##diárese só por precaução
        if match:
            output_file.write("|"+line)