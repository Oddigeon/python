try:
    num = int(input('Введите число: '))
    Pasqal = []

    for i in range(num):
        row = [1] * (i + 1)
        for j in range(i + 1):
            if j != 0 and j != i:
                row[j] = Pasqal[i - 1][j - 1] + Pasqal[i - 1][j]
        Pasqal.append(row)

    for p in Pasqal:
        print(*p)
    
except ValueError:
    print('Natural number was expected')