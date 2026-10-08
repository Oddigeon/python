vektor_a = list(map(float, input().split()))
vektor_b = list(map(float, input().split()))
scalar = 0

for i in range(len(vektor_a)):
    scalar += (vektor_a[i] * vektor_b[i])

print(scalar)