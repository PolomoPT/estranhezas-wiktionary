import mariadb
import json
import re

with open("mycredentials.json", "r", encoding='utf-8') as f:
    credentials = json.load(f)

# Connection details
host = "127.0.0.1"
port = 3306
user = credentials["user"]
password = credentials["password"]
database = "enwiktionary_p"

connection = mariadb.connect(
    host=host,
    port = port,
    user=user,
    password=password,
    database=database
)

# Connect
try:
    with connection.cursor(dictionary=True) as cursor:
        # Get all Portuguese lemmas not in the Brazil pre-1990 category
        sql = """
        SELECT DISTINCT page_title
        FROM page
        JOIN categorylinks ON page_id = cl_from
        WHERE page_namespace = 0
        AND cl_to = "Portuguese_lemmas"
        AND page_id NOT IN (
            SELECT cl_from 
            FROM categorylinks 
            WHERE cl_to IN (
                "Portuguese_forms_superseded_by_AO1990"
            )
        )
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("sem 1990\\lista.txt", "w", encoding="utf-8") as file:
            for result in results:
                page_title = result["page_title"].decode("utf-8")  # Decode bytes to string
                page_title = page_title.replace("_", " ")
                file.write(page_title + "\n")
    with connection.cursor(dictionary=True) as cursor:
        # Get all Portuguese non-lemmas that do not link to pages in the Brazil pre-1990 category
        sql = """
        SELECT DISTINCT page_title
        FROM page
        JOIN categorylinks ON page_id = cl_from
        WHERE page_namespace = 0
        AND cl_to = "Portuguese_non-lemma_forms"
        AND page_id NOT IN (
            SELECT cl_from 
            FROM categorylinks 
            WHERE cl_to IN (
                "Portuguese_forms_superseded_by_AO1990"
            )
        )
        AND page_id NOT IN (
            SELECT DISTINCT pl_from
            FROM pagelinks
            JOIN linktarget ON pl_target_id = lt_id
            JOIN page ON lt_namespace = page_namespace AND lt_title = page_title
            JOIN categorylinks ON page_id = cl_from
            WHERE cl_to = "Portuguese_forms_superseded_by_AO1990"
        )
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("sem 1990\\nonlemma.txt", "w", encoding="utf-8") as file:
            for result in results:
                page_title = result["page_title"].decode("utf-8")  # Decode bytes to string
                page_title = page_title.replace("_", " ")
                file.write(page_title + "\n")
                
finally:
    connection.close()

##
## ÓI
##

input_file_path = 'sem 1990\\lista.txt'
output_file_path = 'sem 1990\\com_ói.txt'

with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        match = re.search('ói(?=.)(?! )(?!-)(?!s )(?!s-)(?!s$)(?!deo)(?!dea)', line)
        match_not = re.search('(er|eres)(?!\\S)', line)
        if match and not match_not:
            output_file.write("|"+line)

nonlemma_file_path = 'sem 1990\\nonlemma.txt'

with open(nonlemma_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'a', encoding='utf-8') as output_file:
    for line in input_file:
        match = re.search('ói(?=.)(?! )(?!-)(?!s )(?!s-)(?!s$)(?!deo)(?!dea)', line)
        match_not = re.search('(er|eres)(?!\\S)', line)
        if match and not match_not:
            output_file.write("|"+line)

##
## HÍFENS
##

hifen_file_path = 'sem 1990\\tem hífen\\com_hifen.txt'

with open(input_file_path, 'r', encoding='utf-8') as input_file, open(hifen_file_path, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        match_hyphen = re.search('.*-.*', line)
        match_prefix = re.search('-$', line)
        match_suffix = re.search('^-', line)
        if not match_prefix and not match_suffix:
            if match_hyphen:
                output_file.write(line)

#

conectivo_file_path = 'sem 1990\\tem hífen\\com_conectivo.txt'

with open(hifen_file_path, 'r', encoding='utf-8') as input_file, open(conectivo_file_path, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        match_conectivo = re.search('-.*-', line)
        match_exceções = re.search('água-de-colônia|arco-da-velha|cor-de-rosa|mais-que-perfeito|pé-de-meia', line)
        if match_conectivo and not match_exceções:
            output_file.write("|"+line)

#

caminho_prefixo = 'sem 1990\\tem hífen\\com_prefixo.txt'
caminho_fallback = 'sem 1990\\tem hífen\\fallback.txt'
caminho_ultrafallback = 'sem 1990\\tem hífen\\ultrafallback.txt'

arquivo_input = open(hifen_file_path, 'r', encoding='utf-8')
arquivo_prefixo = open(caminho_prefixo, 'w', encoding='utf-8')
arquivo_fallback = open(caminho_fallback, 'w', encoding='utf-8')
arquivo_ultrafallback = open(caminho_ultrafallback, 'w', encoding='utf-8')

for line in arquivo_input:
    match_conectivo = re.search('-.*-', line)
    match_sempre_com_hifen = re.search('(além|aquém|bem|ex|pós|pré|pró|recém|sem|vice)-', line)
    match_prefixo_a = re.search('(?<!\\S)(contra|extra|infra|intra|mega|supra|ultra)-(?!a|á|à|â|ã|h)', line)
    match_prefixo_e = re.search('(?<!\\S)(ante|entre|sobre|tele)-(?!e|é|ê|h)', line)
    match_prefixo_i = re.search('(?<!\\S)(alvi|anti|arqui|maxi|multi|pluri|poli|semi|tri)-(?!i|í|h)', line)
    match_prefixo_o = re.search('(?<!\\S)(aero|agro|anarco|auto|ciclo|eletro|foto|geo|hidro|macro|micro|moto|nano|neo|proto|pseudo|retro|socio|vaso|video)-(?!o|ó|ô|õ|h)', line)
    match_in_des = re.search('(?<!\\S)(des|in)-h', line)
    match_m_n = re.search('(?<!\\S)(circum|pan)-(?!h|m|n|a|á|à|â|ã|e|é|ê|i|í|o|ó|ô|õ|u|ú)', line)
    match_b =  re.search('(?<!\\S)(sob|sub)-(?!h|r|b)', line)
    match_mal =  re.search('(?<!\\S)mal-(?!h|a|á|à|â|ã|e|é|ê|i|í|o|ó|ô|õ|u|ú)', line)
    match_co_re = re.search('(?<!\\S)(co|re)-(?!h)', line)
    match_a = re.search('a-(?!a|á|à|â|ã|h)', line)
    match_e = re.search('e-(?!e|é|ê|h)', line)
    match_i = re.search('i-(?!i|í|h)', line)
    match_o = re.search('o-(?!o|ó|ô|õ|h)', line)
    match_u = re.search('u-(?!u|ú|h)', line)
    if not match_conectivo and not match_sempre_com_hifen:
        if match_prefixo_a or match_prefixo_e or match_prefixo_i or match_prefixo_o or match_in_des or match_m_n or match_b or match_mal or match_co_re:
            arquivo_prefixo.write("|"+line)
        elif match_a or match_e or match_i or match_o or match_u:
            arquivo_fallback.write("|"+line)
        elif not match_prefixo_a and not match_prefixo_e and not match_prefixo_i and not match_prefixo_o and not match_in_des and not match_m_n and not match_b and not match_mal and not match_co_re and not match_a and not match_e and not match_i and not match_o and not match_u:
            arquivo_ultrafallback.write("|"+line)