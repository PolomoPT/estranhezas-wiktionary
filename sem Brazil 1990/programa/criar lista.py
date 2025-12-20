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
        # Get all Portuguese lemmas not in the category
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
                "Brazilian_Portuguese_forms_superseded_by_AO1990"
            )
        )
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("sem Brazil 1990\\lista.txt", "w", encoding="utf-8") as file:
            for result in results:
                page_title = result["page_title"].decode("utf-8")
                page_title = page_title.replace("_", " ")
                file.write(page_title + "\n")
    with connection.cursor(dictionary=True) as cursor:
        # Get all Portuguese non-lemmas that do not link to pages in the category
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
                "Brazilian_Portuguese_forms_superseded_by_AO1990"
            )
        )
        AND page_id NOT IN (
            SELECT DISTINCT pl_from
            FROM pagelinks
            JOIN linktarget ON pl_target_id = lt_id
            JOIN page ON lt_namespace = page_namespace AND lt_title = page_title
            JOIN categorylinks ON page_id = cl_from
            WHERE cl_to = "Brazilian_Portuguese_forms_superseded_by_AO1990"
        )
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("sem Brazil 1990\\lista.txt", "a", encoding="utf-8") as file:
            for result in results:
                page_title = result["page_title"].decode("utf-8")
                page_title = page_title.replace("_", " ")
                file.write(page_title + "\n")
                
finally:
    connection.close()

input_file_path = 'sem Brazil 1990\\lista.txt'
ü_file_path = 'sem Brazil 1990\\com_ü_etc.txt'

with open(input_file_path, 'r', encoding='utf-8') as input_file, open(ü_file_path, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        match_ü = re.search('(q|g)ü(e|é|ê|è|i|í|ì|ï)', line)
        if match_ü:
            output_file.write("|"+line)

éi_file_path = 'sem Brazil 1990\\com_éi_etc.txt'

with open(input_file_path, 'r', encoding='utf-8') as input_file, open(éi_file_path, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        match = re.search('éi(?=.)(?! )(?!-)(?!s )(?!s-)(?!s$)(?!deo)', line)
        match_not = re.search('(er|eres)(?!\\S)', line)
        if match and not match_not:
            output_file.write("|"+line)
