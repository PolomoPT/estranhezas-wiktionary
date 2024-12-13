# 1911 ou 1943
try:
    with open("1911 ou 1943\\programa\\criar lista.py", encoding='utf-8') as f:
        exec(f.read())
    print("Executed 'criar lista.py' in 1911 ou 1943")
    with open("1911 ou 1943\\programa\\acento.py", encoding='utf-8') as f:
        exec(f.read())
except Exception as e:
    print(f"Error executing '1911 ou 1943\\programa\\criar lista.py': {e}")

# 1911 ou 1943 non-lemma
try:
    with open("1911 ou 1943 non-lemma\\programa\\criar lista.py", encoding='utf-8') as f:
        exec(f.read())
    print("Executed 'criar lista.py' in 1911 ou 1943 non-lemma")
except Exception as e:
    print(f"Error executing '1911 ou 1943 non-lemma\\programa\\criar lista.py': {e}")

# 1945
try:
    with open("sem 1945\\programa\\criar lista.py", encoding='utf-8') as f:
        exec(f.read())
    print("Executed 'criar lista.py' in sem 1945")
except Exception as e:
    print(f"Error executing 'sem 1945\\programa\\criar lista.py': {e}")

# 1990
try:
    with open("sem Brazil 1990\\programa\\criar lista.py", encoding='utf-8') as f:
        exec(f.read())
    print("Executed 'criar lista.py' in sem Brazil 1990")
    with open("sem Brazil 1990\\programa\\dierese.py", encoding='utf-8') as f:
        exec(f.read())
    with open("sem Brazil 1990\\programa\\ei.py", encoding='utf-8') as f:
        exec(f.read())
except Exception as e:
    print(f"Error executing 'sem Brazil 1990\\programa\\criar lista.py': {e}")