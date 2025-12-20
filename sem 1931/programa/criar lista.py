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
        # Get all Portuguese lemmas in the 1931 category
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
                "Portuguese_forms_prescribed_by_the_1931_Agreement"
            )
        )
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("sem 1931\\lista.txt", "w", encoding="utf-8") as file:
            for result in results:
                page_title = result["page_title"].decode("utf-8")  # Decode bytes to string
                page_title = page_title.replace("_", " ")
                file.write(page_title + "\n")
    with connection.cursor(dictionary=True) as cursor:
        # Get all Portuguese non-lemmas that do not link to pages in the 1931 category
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
                "Portuguese_forms_prescribed_by_the_1931_Agreement"
            )
        )
        AND page_id NOT IN (
            SELECT DISTINCT pl_from
            FROM pagelinks
            JOIN linktarget ON pl_target_id = lt_id
            JOIN page ON lt_namespace = page_namespace AND lt_title = page_title
            JOIN categorylinks ON page_id = cl_from
            WHERE cl_to = "Portuguese_forms_prescribed_by_the_1931_Agreement"
        )
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("sem 1931\\lista.txt", "a", encoding="utf-8") as file:
            for result in results:
                page_title = result["page_title"].decode("utf-8")  # Decode bytes to string
                page_title = page_title.replace("_", " ")
                file.write(page_title + "\n")
                
finally:
    connection.close()


input_file_path = 'sem 1931\\lista.txt'
output_file_path = 'sem 1931\\oxitonas_sem_marcacao.txt'

with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        match_exceções = re.search('(cú|nú)( |-)', line) or re.search('(cú|nú)$', line) or re.search('^(í|ú)$', line)
        match_busca = re.search('(?<![a|e|ei|o|u])(í|ú|ís|ús)$', line) or re.search('(?<![a|e|ei|o|u])(í|ú|ís|ús)( |-)', line)
        if match_busca and not match_exceções:
            output_file.write("|"+line)

output_file_path = 'sem 1931\\paroxitonas.txt'

with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        match_busca = re.search('(?<=[á|é|í|ó|ú]).*(i|u|is|us)$', line) or re.search('(?<=[á|é|í|ó|ú]).*(i|u|is|us)( |-)', line)
        if match_busca:
            output_file.write("|"+line)