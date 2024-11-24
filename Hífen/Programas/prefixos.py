import re

caminho_input = 'Hífen\\com_hifen.txt'

caminho_vogais = 'Hífen\\sem_vogais_iguais.txt'
caminho_b = 'Hífen\\com_b.txt'
caminho_co_re = 'Hífen\\com_co_re.txt'
caminho_in_des = 'Hífen\\com_in_des.txt'
caminho_m_n = 'Hífen\\com_m_n.txt'
caminho_mal = 'Hífen\\com_mal.txt'
caminho_fallback = 'Hífen\\fallback.txt'
caminho_ultrafallback = 'Hífen\\ultrafallback.txt'


arquivo_input = open(caminho_input, 'r', encoding='utf-8')

arquivo_vogais = open(caminho_vogais, 'w', encoding='utf-8')
arquivo_b = open(caminho_b, 'w', encoding='utf-8')
arquivo_co_re = open(caminho_co_re, 'w', encoding='utf-8')
arquivo_in_des = open(caminho_in_des, 'w', encoding='utf-8')
arquivo_m_n = open(caminho_m_n, 'w', encoding='utf-8')
arquivo_mal = open(caminho_mal, 'w', encoding='utf-8')
arquivo_fallback = open(caminho_fallback, 'w', encoding='utf-8')
arquivo_ultrafallback = open(caminho_ultrafallback, 'w', encoding='utf-8')

for line in arquivo_input:
    match_connectivo = re.search('-.*-', line)
    match_sempre_com_hifen = re.search('(além|aquém|bem|ex|pós|pré|pró|recém|sem|vice)-', line)
    match_prefixo_a = re.search('(^|\\s)(contra|extra|infra|intra|mega|supra|ultra)-(?!a|á|à|â|ã|h)', line)
    match_prefixo_e = re.search('(^|\\s)(ante|entre|sobre|tele)-(?!e|é|ê|h)', line)
    match_prefixo_i = re.search('(^|\\s)(alvi|anti|arqui|maxi|multi|pluri|poli|semi|tri)-(?!i|í|h)', line)
    match_prefixo_o = re.search('(^|\\s)(aero|agro|anarco|auto|ciclo|eletro|foto|geo|hidro|macro|micro|moto|nano|neo|proto|pseudo|retro|socio|vaso|video)-(?!o|ó|ô|õ|h)', line)
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
    if not match_connectivo and not match_sempre_com_hifen:
        if not match_in_des and not match_m_n and not match_b and not match_mal and not match_co_re:
            if match_prefixo_a or match_prefixo_e or match_prefixo_i or match_prefixo_o:
                arquivo_vogais.write("|"+line)
        if not match_prefixo_a and not match_prefixo_e and not match_prefixo_i and not match_prefixo_o and not match_in_des and not match_m_n and not match_mal and not match_co_re:
            if match_b:
                arquivo_b.write("|"+line)
        if not match_prefixo_a and not match_prefixo_e and not match_prefixo_i and not match_prefixo_o and not match_in_des and not match_m_n and not match_b and not match_mal:
            if match_co_re:
                arquivo_co_re.write("|"+line)
        if not match_prefixo_a and not match_prefixo_e and not match_prefixo_i and not match_prefixo_o and not match_m_n and not match_b and not match_mal and not match_co_re:
            if match_in_des:
                arquivo_in_des.write("|"+line)
        if not match_prefixo_a and not match_prefixo_e and not match_prefixo_i and not match_prefixo_o and not match_in_des and not match_b and not match_mal and not match_co_re:
            if match_m_n:
                arquivo_m_n.write("|"+line)
        if not match_prefixo_a and not match_prefixo_e and not match_prefixo_i and not match_prefixo_o and not match_in_des and not match_m_n and not match_b and not match_co_re:
            if match_mal:
                arquivo_mal.write("|"+line)
        if not match_prefixo_a and not match_prefixo_e and not match_prefixo_i and not match_prefixo_o and not match_in_des and not match_m_n and not match_b and not match_mal and not match_co_re:
            if match_a or match_e or match_i or match_o:
                arquivo_fallback.write("|"+line)
        if not match_prefixo_a and not match_prefixo_e and not match_prefixo_i and not match_prefixo_o and not match_in_des and not match_m_n and not match_b and not match_mal and not match_co_re and not match_a and not match_e and not match_i and not match_o and not match_u:
            arquivo_ultrafallback.write("|"+line)