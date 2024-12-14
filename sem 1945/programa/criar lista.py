import mariadb
import json

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
        # Get all Portuguese lemmas not in the pre-1945 category
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
                "Portuguese_forms_superseded_in_1945"
            )
        )
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("sem 1945\\lista.txt", "w", encoding="utf-8") as file:
            for result in results:
                page_title = result["page_title"].decode("utf-8")  # Decode bytes to string
                page_title = page_title.replace("_", " ")
                file.write(page_title + "\n")
    with connection.cursor(dictionary=True) as cursor:
        # Get all Portuguese non-lemmas that do not link to pages in the pre-1945 category
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
                "Portuguese_forms_superseded_in_1945"
            )
        )
        AND page_id NOT IN (
            SELECT DISTINCT pl_from
            FROM pagelinks
            JOIN categorylinks ON page_title
            WHERE cl_to = "Portuguese_forms_superseded_in_1945"
        )
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("sem 1945\\lista.txt", "a", encoding="utf-8") as file:
            for result in results:
                page_title = result["page_title"].decode("utf-8")  # Decode bytes to string
                page_title = page_title.replace("_", " ")
                file.write(page_title + "\n")
                
finally:
    connection.close()