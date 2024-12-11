import pymysql
import json

with open("mycredentials.json", "r") as f:
    credentials = json.load(f)

# Connection details
host = "s4.analytics.db.svc.wikimedia.cloud"
user = credentials["user"]
password = credentials["password"]
database = "enwiktionary_p"

# Establish the connection
connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    database=database,
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
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
                         "Portuguese forms superseded by AO1990", 
                         "Brazilian Portuguese forms superseded by AO1990", 
                         "European Portuguese forms superseded by AO1990"
                     )
                 );"""
        cursor.execute(sql)
        results = cursor.fetchall()
        
        # Open the file to write the results
        with open("sem Brazil 1990\\lemmas.txt", "w", encoding="utf-8") as file:
            # Write each page_title to the file
            for result in results:
                file.write(result["page_title"] + "\n")
                
finally:
    connection.close()
