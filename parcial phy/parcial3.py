n = int(input("Ingrese el número de términos de la serie Fibonacci que desea mostrar: "))

a, b = 0, 1

fibonacci = [a]

for i in range(1, n):
    fibonacci.append(b)
    a, b = b, a + b

suma_fibonacci = sum(fibonacci)

print("Los primeros", n, "términos de la serie Fibonacci son:")
print(fibonacci)
print("La suma de los primeros", n, "términos de la serie Fibonacci es:", suma_fibonacci)
