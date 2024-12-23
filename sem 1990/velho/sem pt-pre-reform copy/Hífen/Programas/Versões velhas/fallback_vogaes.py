import re

input_file_path = 'Hífen\\com_hyphen.txt'
output_file_path = 'Hífen\\fallback_sem_vogaes_iguaes.txt'

with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        match_connectivo = re.search('-.*-', line)
        match_sempre_hyphen = re.search('(além|aquém|bem|ex|pós|pré|pró|recém|sem|vice)', line)
        match_prefixo_a = re.search('(^|\\s)(contra|extra|infra|intra|mega|supra|ultra)-(?!a|á|à|â|ã|h)', line)
        match_prefixo_e = re.search('(^|\\s)(ante|entre|sobre|tele)-(?!e|é|ê|h)', line)
        match_prefixo_i = re.search('(^|\\s)(alvi|anti|arqui|maxi|multi|pluri|poli|semi|tri)-(?!i|í|h)', line)
        match_prefixo_o = re.search('(^|\\s)(aero|agro|auto|ciclo|eletro|foto|geo|hidro|macro|micro|moto|nano|neo|proto|pseudo|retro|socio|vaso|video)-(?!o|ó|ô|õ|h)', line)
        match_in_des = re.search('(^|\\s)(des|in)-h', line)
        match_m_n = re.search('(^|\\s)(circum|pan)-(?!h|m|n|a|á|à|â|ã|e|é|ê|i|í|o|ó|ô|õ|u|ú)', line)
        match_b =  re.search('(^|\\s)(sob|sub)-(?!h|r|b)', line)
        match_mal =  re.search('(^|\\s)mal-(?!h|a|á|à|â|ã|e|é|ê|i|í|o|ó|ô|õ|u|ú)', line)
        match_co_re = re.search('(^|\\s)(co|re)-(?!h)', line)
        match_a = re.search('a-(?!a|á|à|â|ã|h)', line)
        match_e = re.search('e-(?!e|é|ê|h)', line)
        match_i = re.search('i-(?!i|í|h)', line)
        match_o = re.search('o-(?!o|ó|ô|õ|h)', line)
        match_u = re.search('u-(?!u|ú|h)', line)
        if not match_connectivo and not match_sempre_hyphen and not match_prefixo_a and not match_prefixo_e and not match_prefixo_i and not match_prefixo_o and not match_in_des and not match_m_n and not match_b and not match_mal and not match_co_re:
            if match_a or match_e or match_i or match_o:
                output_file.write("|"+line)