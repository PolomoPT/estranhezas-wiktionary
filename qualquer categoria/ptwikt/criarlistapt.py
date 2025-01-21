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
database = "ptwiktionary_p"

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
        AND cl_to IN ("Abreviatura_(Português)", "Acrônimo_(Português)", "Sigla_(Português)")
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("qualquer categoria\\ptwikt\\pt\\abreviaturas.txt", "w", encoding="utf-8") as file:
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
        AND cl_to IN ("Adjetivo_(Português)", "Locução_adjetiva_(Português)", "Superlativo_(Português)")
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("qualquer categoria\\ptwikt\\pt\\adjetivos.txt", "w", encoding="utf-8") as file:
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
        AND cl_to IN ("Advérbio_(Português)", "Locução adverbial_(Português)")
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("qualquer categoria\\ptwikt\\pt\\advérbios.txt", "w", encoding="utf-8") as file:
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
        AND cl_to = "Artigo_(Português)"
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("qualquer categoria\\ptwikt\\pt\\artigos.txt", "w", encoding="utf-8") as file:
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
        AND cl_to IN ("Conjunção_(Português)", "Locução_conjuntiva_(Português)")
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("qualquer categoria\\ptwikt\\pt\\conjunções.txt", "w", encoding="utf-8") as file:
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
        AND cl_to = "Contração_(Português)"
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("qualquer categoria\\ptwikt\\pt\\contrações.txt", "w", encoding="utf-8") as file:
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
        AND cl_to IN ("Interjeição_(Português)", "Locução_interjetiva_(Português)")
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("qualquer categoria\\ptwikt\\pt\\interjeições.txt", "w", encoding="utf-8") as file:
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
        AND cl_to IN ("Locução_(Português)", "Provérbio_(Português)", "Expressão_(Português)")
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("qualquer categoria\\ptwikt\\pt\\locuções.txt", "w", encoding="utf-8") as file:
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
        AND cl_to IN ("Morfema_(Português)", "Interfixo_(Português)", "Pospositivo_(Português)", "Prefixo_(Português)", "Sufixo_(Português)")
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("qualquer categoria\\ptwikt\\pt\\morfemas.txt", "w", encoding="utf-8") as file:
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
        AND cl_to IN ("Numeral_(Português)", "Numeral_cardinal_(Português)", "Numeral_fracionário_(Português)", "Numeral_multiplicativo_(Português)", "Numeral_ordinal_(Português)") 
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("qualquer categoria\\ptwikt\\pt\\numerais.txt", "w", encoding="utf-8") as file:
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
        AND cl_to IN ("Preposição_(Português)", "Locução_prepositiva_(Português)")
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("qualquer categoria\\ptwikt\\pt\\preposições.txt", "w", encoding="utf-8") as file:
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
        AND cl_to IN ("Pronome_(Português)", "Forma_de_pronome_(Português)", "Locução_pronominal_(Português)", "Pronome_pessoal_(Português)")
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("qualquer categoria\\ptwikt\\pt\\pronomes.txt", "w", encoding="utf-8") as file:
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
        AND cl_to IN ("Substantivo_(Português)", "Aumentativo_(Português)", "Locução_substantiva_(Português)") 
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("qualquer categoria\\ptwikt\\pt\\substantivos.txt", "w", encoding="utf-8") as file:
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
        AND cl_to IN ("Verbo_(Português)", "Expressão_verbal_(Português)", "Locução_verbal_(Português)", "Verbo_pronominal_(Português)")
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("qualquer categoria\\ptwikt\\pt\\verbos.txt", "w", encoding="utf-8") as file:
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
        AND cl_to = "Português_galego"
        ORDER BY page_title;"""

        cursor.execute(sql)
        results = cursor.fetchall()
        with open("qualquer categoria\\ptwikt\\pt\\portugalego.txt", "w", encoding="utf-8") as file:
            for result in results:
                page_title = result["page_title"].decode("utf-8")  # Decode bytes to string
                page_title = page_title.replace("_", " ")
                file.write(page_title + "\n")
finally:
    connection.close()