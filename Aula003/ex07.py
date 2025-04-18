print("                                     ")
print("                                     ")
n1 = float(input("Digite o primeira nota: "))
print("                                     ")
n2 = float(input("Digite o segunda nota: "))
print("                                     ")
n3 = float(input("Digite o terceira nota: "))
print("                                     ")
m  = (n1+n2+n3)/3
if m >= 7:
    print(f"Aprovado {m}")
else:
    if m <4:
        print(f"Reprovado {m}")
    else:
        print(f"Em Recuperação {m}")

