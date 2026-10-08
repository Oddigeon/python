first_line = list(map(float, input().split()))
n = int(first_line[0])
x = first_line[1]

a = float(input())
b = float(input())
c = float(input())

der_a = n * a * (x ** (n - 1))
derivative = der_a + b

print(f'{derivative:.3f}')