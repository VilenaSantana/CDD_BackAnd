l = float(input("Quantos litros de gasolina você abasteceu?"))
tg = int(input("Qual tipo de combustivel? Se Gasolina digite 1 ou Etanol digite 2? "))
g = 5.80
e = 4.90
if tg ==1:
    print(f"Você pagou {g*tg} de gasolina")
else:
    print(f"Você pagou {e*tg} de Etanol")
