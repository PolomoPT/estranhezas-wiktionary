import re

input_file_path = 'Hífen\\lemmas.txt'
output_file_path = 'Hífen\\com_hifen.txt'

with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        match_hyphen = re.search('.*-.*', line)
        match_prefix = re.search('-$', line)
        match_suffix = re.search('^-', line)
        if not match_prefix and not match_suffix:
            if match_hyphen:
                output_file.write(line)