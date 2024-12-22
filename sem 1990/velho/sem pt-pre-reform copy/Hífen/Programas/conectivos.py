import re

input_file_path = 'Lemmas_-pt-pre-reform\\Hífen\\com_hifen.txt'
output_file_path = 'Lemmas_-pt-pre-reform\\Hífen\\com_connectivo.txt'

with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        match_connectivo = re.search('-.*-', line)
        match_exceções = re.search('água-de-colônia|arco-da-velha|cor-de-rosa|mais-que-perfeito|pé-de-meia', line)
        if match_connectivo and not match_exceções:
            output_file.write("|"+line)