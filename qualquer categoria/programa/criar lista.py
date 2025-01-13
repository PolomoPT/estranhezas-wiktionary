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
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("qualquer categoria\\lista.txt", "w", encoding="utf-8") as file:
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
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("qualquer categoria\\nonlemma.txt", "w", encoding="utf-8") as file:
            for result in results:
                page_title = result["page_title"].decode("utf-8")  # Decode bytes to string
                page_title = page_title.replace("_", " ")
                file.write(page_title + "\n")
                
finally:
    connection.close()

lemma_file_path = 'qualquer categoria\\lista.txt'
nonlemma_file_path = 'qualquer categoria\\nonlemma.txt'

##
## CO e RE seguido de H
##

co_re_file_path = 'qualquer categoria\\co_re\\co_re.txt'

with open(lemma_file_path, 'r', encoding='utf-8') as input_file, open(co_re_file_path, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        match_co_re = re.search('(?<!\\S)(co|re)-h', line)
        if match_co_re:
            output_file.write("|"+line)

with open(nonlemma_file_path, 'r', encoding='utf-8') as input_file, open(co_re_file_path, 'a', encoding='utf-8') as output_file:
    for line in input_file:
        match_co_re = re.search('(?<!\\S)(co|re)-h', line)
        if match_co_re:
            output_file.write("|"+line)