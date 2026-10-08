def number_float(num):
    
    num = num.strip()

    sign = True
    start = 0

    if num[0] == '-':
        sign = False
        start = 1
    elif num[0] == '+':
        start = 1
    else:
        exit('Ошибка. Введите знак перед числом')

    before_dot = 0
    after_dot = 0
    after_dot_nums = 1
    has_dot = False
    has_digits = False

    for i in range(start, len(num)):
        char = num[i]
        if char == '.':
            if has_dot:
                exit('Ошибка ввода. Несколько точек')
            has_dot = True
        elif '0' <= char <= '9':
            has_digits = True
            digit = ord(char) - ord('0')
            if not has_dot:
                before_dot = before_dot * 10 + digit
            else:
                after_dot = after_dot * 10 + digit
                after_dot_nums *= 10
        else:
            exit('Ошибка. Некорректный ввод.')

    if not has_digits:
        exit('Ошибка. Некорректный ввод')

    if sign:
        value = before_dot + (after_dot / after_dot_nums)
    else:
        value = (before_dot + (after_dot / after_dot_nums)) * (-1)
    
    return value

number = input()

if not number:
    print('Ошибка. Введите число')
else:
    value = number_float(number)
    result = value * 2
    print(f'{result:.3f}')
