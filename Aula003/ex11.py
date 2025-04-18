t = input("qual tipo de combustive\n"
          "G para Gasolina\n"
          "E para Etanol ")
q = float(input("Quantos litros? "))
vg = 5.8
ve = 4.9
if t == "G" or t == "g":
    v = vg * q
elif t == "e" or "E":
        v = ve * q
else:
    print("Tipo de combustivel invalido")
print(f"Você gastou R${v:.2f}")

