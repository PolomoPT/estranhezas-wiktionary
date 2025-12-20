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
        sql = """
        SELECT DISTINCT page_title
        FROM page
        JOIN categorylinks ON page_id = cl_from
        WHERE page_namespace = 0
        AND cl_to IN ("Portuguese_forms_superseded_in_1911", "Portuguese_forms_superseded_in_1943")
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("1911 ou 1943\\lista.txt", "w", encoding="utf-8") as file:
            for result in results:
                page_title = result["page_title"].decode("utf-8")
                page_title = page_title.replace("_", " ")
                file.write(page_title + "\n")
                
finally:
    connection.close()

##
## PRÉ-1911 COM ACENTO
##

input_file_path = '1911 ou 1943\\lista.txt'
output_file_path = '1911 ou 1943\\com acento.txt'

with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        match = re.search('â|á|à|ä|ê|é|è|ë|í|ì|ï|ô|ó|ò|ö|ú|ù|ü', line) ##diérese só por precaução
        if match:
            output_file.write("|"+line)