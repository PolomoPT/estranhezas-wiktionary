# 1911 ou 1943
try:
    with open("1911 ou 1943\\criar lemmas.py", encoding='utf-8') as f:
        exec(f.read())
    print("Executed 'criar lemmas.py' in 1911 ou 1943")
    with open("1911 ou 1943\\com acento.py", encoding='utf-8') as f:
        exec(f.read())
except Exception as e:
    print(f"Error executing '1911 ou 1943\\criar lemmas.py': {e}")

# 1911 ou 1943 non-lemma
try:
    with open("1911 ou 1943 non-lemma\\criar lemmas.py", encoding='utf-8') as f:
        exec(f.read())
    print("Executed 'criar lemmas.py' in 1911 ou 1943 non-lemma")
except Exception as e:
    print(f"Error executing '1911 ou 1943 non-lemma\\criar lemmas.py': {e}")

# 1945
try:
    with open("sem 1945\\criar lemmas.py", encoding='utf-8') as f:
        exec(f.read())
    print("Executed 'criar lemmas.py' in sem 1945")
except Exception as e:
    print(f"Error executing 'sem 1945\\criar lemmas.py': {e}")

# 1990
try:
    with open("sem Brazil 1990\\criar lemmas.py", encoding='utf-8') as f:
        exec(f.read())
    print("Executed 'criar lemmas.py' in sem Brazil 1990")
    with open("sem Brazil 1990\\dierese.py", encoding='utf-8') as f:
        exec(f.read())
    with open("sem Brazil 1990\\ei.py", encoding='utf-8') as f:
        exec(f.read())
except Exception as e:
    print(f"Error executing 'sem Brazil 1990\\criar lemmas.py': {e}")