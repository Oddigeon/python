number = int(input('Введите целое число: '))
number_copy = number
reverse_number = 0

for i in range(len(str(number))):
    reverse_number += number_copy % 10
    number_copy //= 10
    if i < (len(str(number)) - 1):
        reverse_number *= 10

if reverse_number == number:
    print(True)
else:
    print(False)