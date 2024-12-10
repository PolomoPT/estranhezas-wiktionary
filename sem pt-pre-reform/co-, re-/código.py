import re

input_file_path = 'Lemmas_-pt-pre-reform\\lemmas.txt'
output_file_path = "Lemmas_-pt-pre-reform\\co-, re-\\hifenado.txt"

with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        match_co = re.search('^co-', line)
        match_re = re.search('^re-', line)
        if match_co or match_re:
            output_file.write("|"+line)