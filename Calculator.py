a = int(input("Введите 1-е число: "))
b = int(input("Введите 2-е число: "))
user_sign = input("Выберите действие с числами: '+', '-', '*', '/' (печатайте без ' ') : ")

if user_sign == '+':
    print("Результат:", a + b)
elif user_sign == '-':
    print("Результат:", a - b)
elif user_sign == '*':
    print("Результат:", a * b)
elif user_sign == '/':
    try:
        print("Результат", a / b)
    except ZeroDivisionError:
        print("На ноль делить нельзя ¯\_(ツ)_/¯")
elif user_sign != ('+', '-', '*', '/'):
    print("Введите корректный символ")