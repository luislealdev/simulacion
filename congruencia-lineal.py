print("-------------PARÁMETROS-------------")
m = int(input("Ingrese el número de números aleatorios que desee: "))
k = int(input("Ingrese el valor de k: "))
c = int(input("Ingrese el valor de c: "))
x = int(input("Ingrese el valor inicial de x (X0): "))

a = 1 + 4*k

print("-------------RESULTADOS-------------")

for i in range(m):
    x = (a*x + c) % m
    print(f"Valor de R{i+1} = {round(x/(m-1), 3)}")

print("-------------FIN DE PROGRAMA--------")
