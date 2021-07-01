dig1 = input("Первое число:")

if dig1.isdigit() == True:
    dig1 = int(dig1)
else: print('Это не число', stop)

operations=str(input("Выберите одну из операций: (+  -  *  /)\n"))
#else:
#    print("Ввод должен быть числом")

dig2=int(input("Второе число:"))

if operations == "+":
    result = dig1 + dig2
elif operations == "-":
    result = dig1 - dig2
elif operations=="*":
    result = dig1 * dig2
elif operations=="*":
    result = dig1 * dig2
else: print("Неверный выбор")

print("Результат операции:", result)



