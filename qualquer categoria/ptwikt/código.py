import re

abreviaturas = "qualquer categoria\\ptwikt\\pt\\abreviaturas.txt"
adjetivos = "qualquer categoria\\ptwikt\\pt\\adjetivos.txt"
advérbios = "qualquer categoria\\ptwikt\\pt\\advérbios.txt"
artigos = "qualquer categoria\\ptwikt\\pt\\artigos.txt"
conjunções = "qualquer categoria\\ptwikt\\pt\\conjunções.txt"
contrações = "qualquer categoria\\ptwikt\\pt\\contrações.txt"
interjeições = "qualquer categoria\\ptwikt\\pt\\interjeições.txt"
locuções = "qualquer categoria\\ptwikt\\pt\\locuções.txt"
morfemas = "qualquer categoria\\ptwikt\\pt\\morfemas.txt"
numerais = "qualquer categoria\\ptwikt\\pt\\numerais.txt"
preposições = "qualquer categoria\\ptwikt\\pt\\preposições.txt"
pronomes = "qualquer categoria\\ptwikt\\pt\\pronomes.txt"
substantivos = "qualquer categoria\\ptwikt\\pt\\substantivos.txt"
verbos = "qualquer categoria\\ptwikt\\pt\\verbos.txt"
galego = "qualquer categoria\\ptwikt\\pt\\portugalego.txt"

en_abreviaturas = "qualquer categoria\\ptwikt\\en\\en_abreviaturas.txt"
en_adjetivos = "qualquer categoria\\ptwikt\\en\\en_adjetivos.txt"
en_advérbios = "qualquer categoria\\ptwikt\\en\\en_advérbios.txt"
en_artigos = "qualquer categoria\\ptwikt\\en\\en_artigos.txt"
en_conjunções = "qualquer categoria\\ptwikt\\en\\en_conjunções.txt"
en_contrações = "qualquer categoria\\ptwikt\\en\\en_contrações.txt"
en_interjeições = "qualquer categoria\\ptwikt\\en\\en_interjeições.txt"
en_frases = "qualquer categoria\\ptwikt\\en\\en_frases.txt"
en_provérbios = "qualquer categoria\\ptwikt\\en\\en_provérbios.txt"
en_morfemas = "qualquer categoria\\ptwikt\\en\\en_morfemas.txt"
en_numerais = "qualquer categoria\\ptwikt\\en\\en_numerais.txt"
en_preposições = "qualquer categoria\\ptwikt\\en\\en_preposições.txt"
en_pronomes = "qualquer categoria\\ptwikt\\en\\en_pronomes.txt"
en_substantivos = "qualquer categoria\\ptwikt\\en\\en_substantivos.txt"
en_verbos = "qualquer categoria\\ptwikt\\en\\en_verbos.txt"

diff_abreviaturas = "qualquer categoria\\ptwikt\\resultado\\abreviaturas.txt"
diff_adjetivos = "qualquer categoria\\ptwikt\\resultado\\adjetivos.txt"
diff_advérbios = "qualquer categoria\\ptwikt\\resultado\\advérbios.txt"
diff_artigos = "qualquer categoria\\ptwikt\\resultado\\artigos.txt"
diff_conjunções = "qualquer categoria\\ptwikt\\resultado\\conjunções.txt"
diff_contrações = "qualquer categoria\\ptwikt\\resultado\\contrações.txt"
diff_interjeições = "qualquer categoria\\ptwikt\\resultado\\interjeições.txt"
diff_locuções = "qualquer categoria\\ptwikt\\resultado\\locuções.txt"
diff_morfemas = "qualquer categoria\\ptwikt\\resultado\\morfemas.txt"
diff_numerais = "qualquer categoria\\ptwikt\\resultado\\numerais.txt"
diff_preposições = "qualquer categoria\\ptwikt\\resultado\\preposições.txt"
diff_pronomes = "qualquer categoria\\ptwikt\\resultado\\pronomes.txt"
diff_substantivos = "qualquer categoria\\ptwikt\\resultado\\substantivos.txt"
diff_verbos = "qualquer categoria\\ptwikt\\resultado\\verbos.txt"

##abreviaturas
with open(abreviaturas, 'r', encoding='utf-8') as file1:
    with open(en_abreviaturas, 'r', encoding='utf-8') as file2:
        same = set(file1).difference(file2)
    same = sorted(same)
with open(diff_abreviaturas, 'w', encoding='utf-8') as file_out:
    with open(galego, 'r', encoding='utf-8') as file_galego:
        linha = set(file_galego)
    for line in same:
        if line not in linha:
            file_out.write('|'+line)
        elif line in linha:
            file_out.write('|'+line.strip()+'<qq:has gl>\n')

##adjetivos
with open(adjetivos, 'r', encoding='utf-8') as file1:
    with open(en_adjetivos, 'r', encoding='utf-8') as file2:
        same = set(file1).difference(file2)
    same = sorted(same)
with open(diff_adjetivos, 'w', encoding='utf-8') as file_out:
    with open(galego, 'r', encoding='utf-8') as file_galego:
        linha = set(file_galego)
    for line in same:
        if line not in linha:
            file_out.write('|'+line)
        elif line in linha:
            file_out.write('|'+line.strip()+'<qq:has gl>\n')

##advérbios
with open(advérbios, 'r', encoding='utf-8') as file1:
    with open(en_advérbios, 'r', encoding='utf-8') as file2:
        same = set(file1).difference(file2)
    same = sorted(same)
with open(diff_advérbios, 'w', encoding='utf-8') as file_out:
    with open(galego, 'r', encoding='utf-8') as file_galego:
        linha = set(file_galego)
    for line in same:
        if line not in linha:
            file_out.write('|'+line)
        elif line in linha:
            file_out.write('|'+line.strip()+'<qq:has gl>\n')

##artigos
with open(artigos, 'r', encoding='utf-8') as file1:
    with open(en_artigos, 'r', encoding='utf-8') as file2:
        same = set(file1).difference(file2)
    same = sorted(same)
with open(diff_artigos, 'w', encoding='utf-8') as file_out:
    with open(galego, 'r', encoding='utf-8') as file_galego:
        linha = set(file_galego)
    for line in same:
        if line not in linha:
            file_out.write('|'+line)
        elif line in linha:
            file_out.write('|'+line.strip()+'<qq:has gl>\n')

##conjunções
with open(conjunções, 'r', encoding='utf-8') as file1:
    with open(en_conjunções, 'r', encoding='utf-8') as file2:
        same = set(file1).difference(file2)
    same = sorted(same)
with open(diff_conjunções, 'w', encoding='utf-8') as file_out:
    with open(galego, 'r', encoding='utf-8') as file_galego:
        linha = set(file_galego)
    for line in same:
        if line not in linha:
            file_out.write('|'+line)
        elif line in linha:
            file_out.write('|'+line.strip()+'<qq:has gl>\n')

##contrações
with open(contrações, 'r', encoding='utf-8') as file1:
    with open(en_contrações, 'r', encoding='utf-8') as file2:
        same = set(file1).difference(file2)
    same = sorted(same)
with open(diff_contrações, 'w', encoding='utf-8') as file_out:
    with open(galego, 'r', encoding='utf-8') as file_galego:
        linha = set(file_galego)
    for line in same:
        if line not in linha:
            file_out.write('|'+line)
        elif line in linha:
            file_out.write('|'+line.strip()+'<qq:has gl>\n')

##interjeições
with open(interjeições, 'r', encoding='utf-8') as file1:
    with open(en_interjeições, 'r', encoding='utf-8') as file2:
        same = set(file1).difference(file2)
    same = sorted(same)
with open(diff_interjeições, 'w', encoding='utf-8') as file_out:
    with open(galego, 'r', encoding='utf-8') as file_galego:
        linha = set(file_galego)
    for line in same:
        if line not in linha:
            file_out.write('|'+line)
        elif line in linha:
            file_out.write('|'+line.strip()+'<qq:has gl>\n')

##locuções
with open(locuções, 'r', encoding='utf-8') as file1:
    with open(en_frases, 'r', encoding='utf-8') as file2:
        with open(en_provérbios, 'r', encoding='utf-8') as file3:
            same = set(file1).difference(file2)
            same = same.difference(file3)
            same = sorted(same)
with open(diff_locuções, 'w', encoding='utf-8') as file_out:
    with open(galego, 'r', encoding='utf-8') as file_galego:
        linha = set(file_galego)
    for line in same:
        if line not in linha:
            file_out.write('|'+line)
        elif line in linha:
            file_out.write('|'+line.strip()+'<qq:has gl>\n')

##morfemas
with open(morfemas, 'r', encoding='utf-8') as file1:
    with open(en_morfemas, 'r', encoding='utf-8') as file2:
        same = set(file1).difference(file2)
    same = sorted(same)
with open(diff_morfemas, 'w', encoding='utf-8') as file_out:
    with open(galego, 'r', encoding='utf-8') as file_galego:
        linha = set(file_galego)
    for line in same:
        if line not in linha:
            file_out.write('|'+line)
        elif line in linha:
            file_out.write('|'+line.strip()+'<qq:has gl>\n')

##numerais
with open(numerais, 'r', encoding='utf-8') as file1:
    with open(en_numerais, 'r', encoding='utf-8') as file2:
        same = set(file1).difference(file2)
    same = sorted(same)
with open(diff_numerais, 'w', encoding='utf-8') as file_out:
    with open(galego, 'r', encoding='utf-8') as file_galego:
        linha = set(file_galego)
    for line in same:
        if line not in linha:
            file_out.write('|'+line)
        elif line in linha:
            file_out.write('|'+line.strip()+'<qq:has gl>\n')

##preposições
with open(preposições, 'r', encoding='utf-8') as file1:
    with open(en_preposições, 'r', encoding='utf-8') as file2:
        same = set(file1).difference(file2)
    same = sorted(same)
with open(diff_preposições, 'w', encoding='utf-8') as file_out:
    with open(galego, 'r', encoding='utf-8') as file_galego:
        linha = set(file_galego)
    for line in same:
        if line not in linha:
            file_out.write('|'+line)
        elif line in linha:
            file_out.write('|'+line.strip()+'<qq:has gl>\n')

##pronomes
with open(pronomes, 'r', encoding='utf-8') as file1:
    with open(en_pronomes, 'r', encoding='utf-8') as file2:
        same = set(file1).difference(file2)
    same = sorted(same)
with open(diff_pronomes, 'w', encoding='utf-8') as file_out:
    with open(galego, 'r', encoding='utf-8') as file_galego:
        linha = set(file_galego)
    for line in same:
        if line not in linha:
            file_out.write('|'+line)
        elif line in linha:
            file_out.write('|'+line.strip()+'<qq:has gl>\n')

##substantivos
with open(substantivos, 'r', encoding='utf-8') as file1:
    with open(en_substantivos, 'r', encoding='utf-8') as file2:
        same = set(file1).difference(file2)
    same = sorted(same)
with open(diff_substantivos, 'w', encoding='utf-8') as file_out:
    with open(galego, 'r', encoding='utf-8') as file_galego:
        linha = set(file_galego)
    for line in same:
        if line not in linha:
            file_out.write('|'+line)
        elif line in linha:
            file_out.write('|'+line.strip()+'<qq:has gl>\n')

##verbos
with open(verbos, 'r', encoding='utf-8') as file1:
    with open(en_verbos, 'r', encoding='utf-8') as file2:
        same = set(file1).difference(file2)
    same = sorted(same)
with open(diff_verbos, 'w', encoding='utf-8') as file_out:
    with open(galego, 'r', encoding='utf-8') as file_galego:
        linha = set(file_galego)
    for line in same:
        if line not in linha:
            file_out.write('|'+line)
        elif line in linha:
            file_out.write('|'+line.strip()+'<qq:has gl>\n')

##
## TABELA
##


def tamanho(filename):
    with open(filename, encoding='utf-8') as f:
        for i, _ in enumerate(f):
            pass
    return i + 1

n_abreviaturas = tamanho(diff_abreviaturas)
n_adjetivos = tamanho(diff_adjetivos)
n_advérbios = tamanho(diff_advérbios)
n_afixos = tamanho(diff_morfemas)
n_artigos = tamanho(diff_artigos)
n_conjunções = tamanho(diff_conjunções)
n_contrações = tamanho(diff_contrações)
n_interjeições = tamanho(diff_interjeições)
n_numerais = tamanho(diff_numerais)
n_substantivos = tamanho(diff_substantivos)
n_preposições = tamanho(diff_preposições)
n_pronomes = tamanho(diff_pronomes)
n_verbos= tamanho(diff_verbos)
n_frases = tamanho(diff_locuções)

soma = n_abreviaturas + n_adjetivos + n_advérbios + n_afixos + n_artigos + n_conjunções + n_contrações + n_interjeições + n_numerais + n_substantivos + n_preposições + n_pronomes + n_verbos + n_frases

with open(r"qualquer categoria\ptwikt\resultado\tabela.txt", 'w') as tabela:
    tabela.write("""==List==

{| class="wikitable sortable" style="margin-left: auto; margin-right: auto; border: none;"
|-
! Part of Speech
! Count
|-""")

with open(r"qualquer categoria\ptwikt\resultado\tabela.txt", 'a') as tabela:
    tabela.write("""
|[[/Other#Abbreviations|Abbreviations]]
| """
+ str(n_abreviaturas) + """
|-""")

with open(r"qualquer categoria\ptwikt\resultado\tabela.txt", 'a') as tabela:
    tabela.write("""
|[[/Adjectives|Adjectives]]
| """
+ str(n_adjetivos) + """
|-""")
    
with open(r"qualquer categoria\ptwikt\resultado\tabela.txt", 'a') as tabela:
    tabela.write("""
|[[/Other#Adverbs|Adverbs]]
| """
+ str(n_advérbios) + """
|-""")

with open(r"qualquer categoria\ptwikt\resultado\tabela.txt", 'a') as tabela:
    tabela.write("""
|[[/Other#Affixes|Affixes]]
| """
+ str(n_afixos) + """
|-""")

with open(r"qualquer categoria\ptwikt\resultado\tabela.txt", 'a') as tabela:
    tabela.write("""
|[[/Other#Articles|Articles]]
| """
+ str(n_artigos) + """
|-""")

with open(r"qualquer categoria\ptwikt\resultado\tabela.txt", 'a') as tabela:
    tabela.write("""
|[[/Other#Conjunctions|Conjunctions]]
| """
+ str(n_conjunções) + """
|-""")

with open(r"qualquer categoria\ptwikt\resultado\tabela.txt", 'a') as tabela:
    tabela.write("""
|[[/Other#Contractions|Contractions]]
| """
+ str(n_contrações) + """
|-""")

with open(r"qualquer categoria\ptwikt\resultado\tabela.txt", 'a') as tabela:
    tabela.write("""
|[[/Other#Interjections|Interjections]]
| """
+ str(n_interjeições) + """
|-""")

with open(r"qualquer categoria\ptwikt\resultado\tabela.txt", 'a') as tabela:
    tabela.write("""
|[[/Other#Numerals|Numerals]]
| """
+ str(n_numerais) + """
|-""")

with open(r"qualquer categoria\ptwikt\resultado\tabela.txt", 'a') as tabela:
    tabela.write("""
|[[/Nouns/1|Nouns]]
| """
+ str(n_substantivos) + """
|-""")

with open(r"qualquer categoria\ptwikt\resultado\tabela.txt", 'a') as tabela:
    tabela.write("""
|[[/Other#Prepositions|Prepositions]]
| """
+ str(n_preposições) + """
|-""")

with open(r"qualquer categoria\ptwikt\resultado\tabela.txt", 'a') as tabela:
    tabela.write("""
|[[/Other#Pronouns|Pronouns]]
| """
+ str(n_pronomes) + """
|-""")

with open(r"qualquer categoria\ptwikt\resultado\tabela.txt", 'a') as tabela:
    tabela.write("""
|[[/Verbs|Verbs]]
| """
+ str(n_verbos) + """
|-""")
    
with open(r"qualquer categoria\ptwikt\resultado\tabela.txt", 'a') as tabela:
    tabela.write("""
|[[/Other#Phrases|Phrases]]
| """
+ str(n_frases) + """
|-
|'''Total'''
| """
+ str(soma) + """
|-
|}
""")







