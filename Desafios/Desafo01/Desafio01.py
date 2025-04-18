# 2 entradas de horario e 1 saida em 12h
e1 = int(input("Diga a hora que você entrou: "))
m1 = int(input("Diga os minutos que você entrou: "))
e2 = int(input("Diga a hora que você entrou: "))
m2 = int(input("Diga os minutos que você entrou: "))

if e1 < 12:
    h1 = e1
else:
    h1 = e1-12
if e2 < 12:
    h2 = e2
else:
    h2 = e2-12
h = h1 + h2

if m1 < 60:
    s1 = m1
else:
    s1 = m1-60
if m2 < 60:
    s2 = m2
else:
    s2 = m2-60
s = m1 + m2
if s > 60:
    hf = h + 1
else:
    hf = h
if s > 60:
    sf = s%60
else:
    sf = s
if sf == 60:
    sf = 0
    hf = 1
if hf > 12:
    hf = (hf/2)+1

print(f"Saída {hf}:{sf}")




# if m1 + m2 <= 59:
#    s = m1 + m2
#else:
#    s = (m1 + m2)/2
#print(f"Saída {h}:{s}") """
