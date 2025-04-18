h1 = int(input("Hora 1"))
m1 = int(input("Min 1"))
h2 = int(input("Min 2"))
m2 = int(input("Hora 2"))
somah = h1 + h2
somam = m1 + m2
if somam >59:
    somah = somah + 1
#    somam = somam - 60
    somam = somam % 60
if somah >=36:
    somah = somah-36
elif somah >24:
    somah = somah-24
elif somah >=12:
    somah = somah - 12
print(somah)
