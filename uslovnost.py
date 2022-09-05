try:
    g = int(input('введите первое число '))
    c: int = int(input('введите второе число  '))
    print("27 + 8 / g % c")
    b = 27 + 8 / g % c
except ZeroDivisionError:
    print('на ноль делить нельзя')
except TypeError:
    print('неправильный тип')
except ValueError:
    print('ошибка типа введеного числа')
else:
    print('good job')
    print(b)