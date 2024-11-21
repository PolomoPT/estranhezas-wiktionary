import re

input_file_path = 'éi-ói\\lemmas.txt'
output_file_path = 'éi-ói\\com_ei_oi.txt'

with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        match_éi = re.search('éi..', line)
        match_ói = re.search('ói..', line)
        match_suffix = re.search('^-', line)
        if match_éi or match_ói:
            output_file.write("|"+line)