# Обработка ввода дополнительных команд
def externalCommands():
    result = input("ждем команду exit или clear")
    if result.lower() == "exit":
        result = "exit"
    elif result.lower() == "clean":
        result = "clean"

# ожидание ввода числа, проверка на число и отлов ошибок
def numeric_inp1():
    try:
        result = float(input('Введите число... '))
        return result
    except ValueError as err:
        print("Это не похоже на число...", err)
    except:
        return None

# Возврат выбора математической операции
def calc_operator():
    result_calc = input("введите +-*/")
    if result_calc != "+" and result_calc != "-" and result_calc != "*" and result_calc != "/" and result_calc.lower() != "exit" and result_calc.lower() != "clean":
        print("не тот знак")
        return False
    elif result_calc == "+":
        return "add"
    elif result_calc == "-":
        return "minus"
    elif result_calc == "*":
        return "multi"
    elif result_calc == "/":
        return "div"
    elif result_calc.lower() == "exit":
        return "exit"
    elif result_calc.lower() == "clean":
        return "clean"
