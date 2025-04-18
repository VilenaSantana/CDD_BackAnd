print("                                     ")
print("                                     ")
t1 = input("Qual o primeiro time? ")
print("                                     ")
g1 = float(input("Quantos gols ele fez: "))
print("                                     ")
t2  = input("Qual o segundo time? ")
print("                                     ")
g2 = float(input("Digite o segunda nota: "))
print("                                     ")

if g1>g2:
    print(t1)
else:
    if g2>g1:
        print(t2)
    else:
        print("Empate")
