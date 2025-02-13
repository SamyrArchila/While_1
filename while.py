#Input

n = int(input("Dijite el valor de n: "))

#Proccesing

s = 0
i = 1
while i<=n:
    s = s + i
    i = i + 1

print("La suma de los " + str(s))