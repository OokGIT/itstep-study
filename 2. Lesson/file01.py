#
# Ожидаем ввод первого числа и проверяем, что введено именно число
dig1 = input("Первое число:")
print(dig1.isdigit())
if True:
     dig1 = int(dig1)


# Ожидаем выбор математической операции. Проверяем, что выбрали одну из предложенных....
operations=str(input("Выберите одну из операций: (+  -  *  /)\n"))
if operations == "+" or operations == "-" or operations == "*" or operations == "/":
#
#... И ожидаем ввод второго числа


# if dig1.isdigit() == True:
# else:
#     print('Это не число')
#     exit()
# #
# # Ожидаем выбор математической операции. Проверяем, что выбрали одну из предложенных....
# operations=str(input("Выберите одну из операций: (+  -  *  /)\n"))
# if operations == "+" or operations == "-" or operations == "*" or operations == "/":
# #
# #... И ожидаем ввод второго числа
#     dig2=input("Второе число:")
#
# else: print("Неверный выбор"), exit()
#
# if dig2.isdigit() == True:
#     dig2 = int(dig2)
# else: print('Это не число'), exit()
# #
# #
#
# if operations == "+":
#     print (dig1, "+",dig2, "=", dig1+dig2)
# elif operations == "-":
#     print (dig1, "-",dig2, "=", dig1-dig2)
# elif operations=="*":
#     print (dig1, "*",dig2, "=", dig1*dig2)
# elif operations=="/":
#     print (dig1, "/",dig2, "=", dig1/dig2)
#
# else: print("Неверный выбор"), exit()
#
