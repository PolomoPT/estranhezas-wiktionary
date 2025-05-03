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
        # Get all Portuguese lemmas not in the pre-1920 category
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
                "Portuguese_forms_superseded_in_1920"
            )
        )
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("sem 1920\\lista.txt", "w", encoding="utf-8") as file:
            for result in results:
                page_title = result["page_title"].decode("utf-8")  # Decode bytes to string
                page_title = page_title.replace("_", " ")
                file.write(page_title + "\n")
    with connection.cursor(dictionary=True) as cursor:
        # Get all Portuguese non-lemmas that do not link to pages in the pre-1920 category
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
                "Portuguese_forms_superseded_in_1920"
            )
        )
        AND page_id NOT IN (
            SELECT DISTINCT pl_from
            FROM pagelinks
            JOIN linktarget ON pl_target_id = lt_id
            JOIN page ON lt_namespace = page_namespace AND lt_title = page_title
            JOIN categorylinks ON page_id = cl_from
            WHERE cl_to = "Portuguese_forms_superseded_in_1920"
        )
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("sem 1920\\lista.txt", "a", encoding="utf-8") as file:
            for result in results:
                page_title = result["page_title"].decode("utf-8")  # Decode bytes to string
                page_title = page_title.replace("_", " ")
                file.write(page_title + "\n")
                
finally:
    connection.close()

input_file_path = 'sem 1920\\lista.txt'
ü_file_path = 'sem 1920\\com_ù_etc.txt'

with open(input_file_path, 'r', encoding='utf-8') as input_file, open(ü_file_path, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        match_ì_ù = re.search('(a|â|á|à|e|ê|é|è|i|í|ì|ï|o|ô|ó|ò|u|ú|ù|ü)(ì|ù)', line) #antecedido por vogal
        match_ù = re.search('(q|g)ù(e|ê|é|è|i|í|ì|ï)', line) #antecedido por <q> <g>
        if match_ì_ù or match_ù:
            output_file.write("|"+line)

mente_file_path = 'sem 1920\\com_mente.txt'

with open(input_file_path, 'r', encoding='utf-8') as input_file, open(mente_file_path, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        match = re.search('[á|é|í|ó|ú][^\\s-]*mente', line)
        if match:
            output_file.write("|"+line)

##TODO: lista de palavras com ü que não tem com ù, lista de palavras com mente que não tem com agudo...