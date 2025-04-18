mes = int(input("Diga um número de 1 a 12: "))
if mes == 1:
    mes = "Janeiro"
elif mes == 2:
    mes = "Fevereiro"
elif mes == 3:
    mes = "Março"
elif mes == 4:
    mes = "Abril"
elif mes == 5:
    mes = "Maio"
elif mes == 6:
    mes = "Junho"
elif mes == 7:
    mes = "Julho"
elif mes == 8:
    mes = "Agosto"
elif mes == 9:
    mes = "Setembro"
elif mes == 10:
    mes = "Outubro"
elif mes == 11:
    mes = "Novembro"
elif mes == 12:
    mes = "Dezembro"
else:
    mes = "Valor Inválido"
print(f"Esse número é referente ao mês {mes}.")
