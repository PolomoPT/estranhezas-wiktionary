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
        # Get all Portuguese lemmas not in pre-1990 categories
        sql = """
        SELECT DISTINCT page_title 
        FROM page 
        JOIN categorylinks ON page_id = cl_from 
        WHERE page_namespace = 0 
        AND cl_to IN ("Portuguese_forms_superseded_in_1911", "Portuguese_forms_superseded_in_1943")
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("1911 ou 1943\\lemmas.txt", "w", encoding="utf-8") as file:
            for result in results:
                page_title = result["page_title"].decode("utf-8")  # Decode bytes to string
                page_title = page_title.replace("_", " ")
                file.write(page_title + "\n")
                
finally:
    connection.close()
