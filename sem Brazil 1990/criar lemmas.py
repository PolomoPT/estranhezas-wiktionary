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

try:
    with connection.cursor(dictionary=True) as cursor:
        # Get all Portuguese lemmas not in pre-1990 categories
        sql = """SELECT DISTINCT page_title 
                 FROM page 
                 JOIN categorylinks ON page_id = cl_from 
                 WHERE page_namespace = 0 
                 AND cl_to = "Portuguese_lemmas" 
                 AND page_id NOT IN (
                     SELECT cl_from 
                     FROM categorylinks 
                     WHERE cl_to IN (
                         "Brazilian Portuguese forms superseded by AO1990"
                     )
                 );"""
        cursor.execute(sql)
        results = cursor.fetchall()
        with open("sem Brazil 1990\\lemmas.txt", "w", encoding="utf-8") as file:
            for result in results:
                file.write(result["page_title"] + "\n")
                
finally:
    connection.close()
