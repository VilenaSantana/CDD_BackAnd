nota1 = float(input("Diga a primeira nota: "))
nota2 = float(input("Diga a segunda nota: "))

media = (nota1+nota2)/2

if media >= 7:
    print(f"Sua média é {media} você está aprovado!")
elif media >= 5:
    print(f"Sua média é {media} você está em recuperação!")
else:
    print(f"Sua média é {media} você está reprovado!")
