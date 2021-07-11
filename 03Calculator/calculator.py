# Ввод числа или результат от предыдущих операций
# Оператор мат.функции

# если "=", то посчитать

# если +-*/ то ожидаем 2 число

# def into_float():
#     try:
#         user_input = input('Ввод:')
#         res = float(user_input)
# #        print(res)
#     except ZeroDivisionError as err:
#         print("На ноль делить нельзя", err)
#     except ValueError as err:
#         print("Это не похоже на число...", err)
#     except:
#         return None
#
# num = into_float()
# print (num)
def externalCommands():
    result = input("ждем команду exit или clear")
    if result.lower() == "exit":
        result = "exit"
    elif result.lower() == "clean":
        result = "clean"

def numeric_inp1():
    try:
        result = float(input('Введите число... '))
        return result
    except ValueError as err:
        print("Это не похоже на число...", err)
    except:
        return None

def numeric_inp2():
    try:
        result = float(input('Введите число... '))
        return result
    except ZeroDivisionError as err:
        print("На ноль делить нельзя", err)
    except ValueError as err:
        print("Это не похоже на число...", err)
    except:
        return None


# Если пользователь начинает ввод с мат.функции, то считаем, что первое число = 0


dig1=numeric_inp1()
operator=operators_inp()
dig2=
try