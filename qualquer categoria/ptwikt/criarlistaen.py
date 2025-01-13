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
        AND cl_to IN ("Portuguese_initialisms", "Portuguese_abbreviations", "Portuguese_acronyms")
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("qualquer categoria\\ptwikt\\en\\en_abreviaturas.txt", "w", encoding="utf-8") as file:
            for result in results:
                page_title = result["page_title"].decode("utf-8")  # Decode bytes to string
                page_title = page_title.replace("_", " ")
                file.write(page_title + "\n")
    with connection.cursor(dictionary=True) as cursor:
        sql = """
        SELECT DISTINCT page_title
        FROM page
        JOIN categorylinks ON page_id = cl_from
        WHERE page_namespace = 0
        AND cl_to = "Portuguese_adjectives"
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("qualquer categoria\\ptwikt\\en\\en_adjetivos.txt", "w", encoding="utf-8") as file:
            for result in results:
                page_title = result["page_title"].decode("utf-8")  # Decode bytes to string
                page_title = page_title.replace("_", " ")
                file.write(page_title + "\n")
    with connection.cursor(dictionary=True) as cursor:
        sql = """
        SELECT DISTINCT page_title
        FROM page
        JOIN categorylinks ON page_id = cl_from
        WHERE page_namespace = 0
        AND cl_to IN ("Portuguese_adverbs", "Portuguese_superlative_adverbs")
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("qualquer categoria\\ptwikt\\en\\en_advérbios.txt", "w", encoding="utf-8") as file:
            for result in results:
                page_title = result["page_title"].decode("utf-8")  # Decode bytes to string
                page_title = page_title.replace("_", " ")
                file.write(page_title + "\n")
    with connection.cursor(dictionary=True) as cursor:
        sql = """
        SELECT DISTINCT page_title
        FROM page
        JOIN categorylinks ON page_id = cl_from
        WHERE page_namespace = 0
        AND cl_to = "Portuguese_articles"
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("qualquer categoria\\ptwikt\\en\\en_artigos.txt", "w", encoding="utf-8") as file:
            for result in results:
                page_title = result["page_title"].decode("utf-8")  # Decode bytes to string
                page_title = page_title.replace("_", " ")
                file.write(page_title + "\n")
    with connection.cursor(dictionary=True) as cursor:
        sql = """
        SELECT DISTINCT page_title
        FROM page
        JOIN categorylinks ON page_id = cl_from
        WHERE page_namespace = 0
        AND cl_to = "Portuguese_conjunctions"
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("qualquer categoria\\ptwikt\\en\\en_conjunções.txt", "w", encoding="utf-8") as file:
            for result in results:
                page_title = result["page_title"].decode("utf-8")  # Decode bytes to string
                page_title = page_title.replace("_", " ")
                file.write(page_title + "\n")
    with connection.cursor(dictionary=True) as cursor:
        sql = """
        SELECT DISTINCT page_title
        FROM page
        JOIN categorylinks ON page_id = cl_from
        WHERE page_namespace = 0
        AND cl_to = "Portuguese_contractions"
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("qualquer categoria\\ptwikt\\en\\en_contrações.txt", "w", encoding="utf-8") as file:
            for result in results:
                page_title = result["page_title"].decode("utf-8")  # Decode bytes to string
                page_title = page_title.replace("_", " ")
                file.write(page_title + "\n")
    with connection.cursor(dictionary=True) as cursor:
        sql = """
        SELECT DISTINCT page_title
        FROM page
        JOIN categorylinks ON page_id = cl_from
        WHERE page_namespace = 0
        AND cl_to = "Portuguese_interjections"
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("qualquer categoria\\ptwikt\\en\\en_interjeições.txt", "w", encoding="utf-8") as file:
            for result in results:
                page_title = result["page_title"].decode("utf-8")  # Decode bytes to string
                page_title = page_title.replace("_", " ")
                file.write(page_title + "\n")
    with connection.cursor(dictionary=True) as cursor:
        sql = """
        SELECT DISTINCT page_title
        FROM page
        JOIN categorylinks ON page_id = cl_from
        WHERE page_namespace = 0
        AND cl_to = "Portuguese_phrases"
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("qualquer categoria\\ptwikt\\en\\en_frases.txt", "w", encoding="utf-8") as file:
            for result in results:
                page_title = result["page_title"].decode("utf-8")  # Decode bytes to string
                page_title = page_title.replace("_", " ")
                file.write(page_title + "\n")
    with connection.cursor(dictionary=True) as cursor:
        sql = """
        SELECT DISTINCT page_title
        FROM page
        JOIN categorylinks ON page_id = cl_from
        WHERE page_namespace = 0
        AND cl_to = "Portuguese_proverbs"
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("qualquer categoria\\ptwikt\\en\\en_provérbios.txt", "w", encoding="utf-8") as file:
            for result in results:
                page_title = result["page_title"].decode("utf-8")  # Decode bytes to string
                page_title = page_title.replace("_", " ")
                file.write(page_title + "\n")
    with connection.cursor(dictionary=True) as cursor:
        sql = """
        SELECT DISTINCT page_title
        FROM page
        JOIN categorylinks ON page_id = cl_from
        WHERE page_namespace = 0
        AND cl_to IN ("Portuguese_suffixes", "Portuguese_interfixes", "Portuguese_prefixes")
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("qualquer categoria\\ptwikt\\en\\en_morfemas.txt", "w", encoding="utf-8") as file:
            for result in results:
                page_title = result["page_title"].decode("utf-8")  # Decode bytes to string
                page_title = page_title.replace("_", " ")
                file.write(page_title + "\n")
    with connection.cursor(dictionary=True) as cursor:
        sql = """
        SELECT DISTINCT page_title
        FROM page
        JOIN categorylinks ON page_id = cl_from
        WHERE page_namespace = 0
        AND cl_to = "Portuguese_numerals" 
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("qualquer categoria\\ptwikt\\en\\en_numerais.txt", "w", encoding="utf-8") as file:
            for result in results:
                page_title = result["page_title"].decode("utf-8")  # Decode bytes to string
                page_title = page_title.replace("_", " ")
                file.write(page_title + "\n")
    with connection.cursor(dictionary=True) as cursor:
        sql = """
        SELECT DISTINCT page_title
        FROM page
        JOIN categorylinks ON page_id = cl_from
        WHERE page_namespace = 0
        AND cl_to = "Portuguese_prepositions"
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("qualquer categoria\\ptwikt\\en\\en_preposições.txt", "w", encoding="utf-8") as file:
            for result in results:
                page_title = result["page_title"].decode("utf-8")  # Decode bytes to string
                page_title = page_title.replace("_", " ")
                file.write(page_title + "\n")
    with connection.cursor(dictionary=True) as cursor:
        sql = """
        SELECT DISTINCT page_title
        FROM page
        JOIN categorylinks ON page_id = cl_from
        WHERE page_namespace = 0
        AND cl_to = "Portuguese_pronouns"
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("qualquer categoria\\ptwikt\\en\\en_pronomes.txt", "w", encoding="utf-8") as file:
            for result in results:
                page_title = result["page_title"].decode("utf-8")  # Decode bytes to string
                page_title = page_title.replace("_", " ")
                file.write(page_title + "\n")
    with connection.cursor(dictionary=True) as cursor:
        sql = """
        SELECT DISTINCT page_title
        FROM page
        JOIN categorylinks ON page_id = cl_from
        WHERE page_namespace = 0
        AND cl_to IN ("Portuguese_nouns", "Portuguese_proper_nouns") 
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("qualquer categoria\\ptwikt\\en\\en_substantivos.txt", "w", encoding="utf-8") as file:
            for result in results:
                page_title = result["page_title"].decode("utf-8")  # Decode bytes to string
                page_title = page_title.replace("_", " ")
                file.write(page_title + "\n")
    with connection.cursor(dictionary=True) as cursor:
        sql = """
        SELECT DISTINCT page_title
        FROM page
        JOIN categorylinks ON page_id = cl_from
        WHERE page_namespace = 0
        AND cl_to = "Portuguese_verbs"
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("qualquer categoria\\ptwikt\\en\\en_verbos.txt", "w", encoding="utf-8") as file:
            for result in results:
                page_title = result["page_title"].decode("utf-8")  # Decode bytes to string
                page_title = page_title.replace("_", " ")
                file.write(page_title + "\n")
finally:
    connection.close()