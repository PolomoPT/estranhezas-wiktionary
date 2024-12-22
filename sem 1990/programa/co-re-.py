import re

input_file_path = 'sem 1990\\lista.txt'
output_file_path = "sem 1990\co-re-.txt"

with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        match_co = re.search('(?<!\\S)co-[^$]', line)
        match_re = re.search('(?<!\\S)re-[^$]', line)
        if match_co or match_re:
            output_file.write("|"+line)