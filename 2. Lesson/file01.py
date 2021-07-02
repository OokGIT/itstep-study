# Ожидаем выбор математической операции. Проверяем, что выбрали одну из предложенных.
operations = str(input("Выберите одну из математических операций: (+  -  *  /)\n"))
if operations != "+" and operations != "-" and operations != "*" and operations != "/":
    print("Выбрана неверная математическая операция")
    exit()

# Ожидаем ввод первого числа и проверяем, что введено именно число
dig1 = input("Первое число:")
if dig1.isdigit() is True:
    dig1 = int(dig1)
#    print (dig1)
else:
    print('введено не число')
    exit()

# Ожидаем ввод второго числа и проверяем, что введено именно число
dig2 = input("Второе число:")
if dig2.isdigit() is True:
    dig2 = int(dig2)
#    print (dig2)
else:
    print('введено не число')
    exit()

# Проводим математические операции с двумя числами
print("Ваш результат:")
if operations == "+":
    print(dig1, "+", dig2, "=", dig1+dig2)
elif operations == "-":
    print(dig1, "-", dig2, "=", dig1-dig2)
elif operations == "*":
    print(dig1, "*", dig2, "=", dig1*dig2)
elif operations == "/":
    print(dig1, "/", dig2, "=", dig1/dig2)
