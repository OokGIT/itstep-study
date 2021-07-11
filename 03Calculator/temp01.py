# def externalCommands():
#     result = input("ждем команду exit или clean")
#     if result.lower() == "exit":
#         result = "exit"
#     elif result.lower() == "clean":
#         result = "clean"
#
#
# print(externalCommands())

def calc_operator():
    result_calc = input("введите +-*/")
    if result_calc != "+" and result_calc != "-" and result_calc != "*" and result_calc != "/":
        print("не тот знак")
        return False
    elif result_calc == "+":
        return "add"
    elif result_calc == "-":
        return "minus"
    elif result_calc == "*":
        return "multi"
    else:
        return "div"

digit1 = 5
digit2 = 5

if calc_operator() == "add":
    print("плюс")
elif calc_operator() == "minus":
    print("минус")
elif calc_operator() == "multi":
    print("умножение")

#
# while calc_operator():
#     if calc_operator() == "add":
#         result = digit1 + digit2
#         print(result)
#     elif calc_operator() == "minus":
#         result = digit1 - digit2
#         print(result)
#     elif calc_operator() == "multi":
#         result = digit1 * digit2
#         print(result)
#     elif calc_operator() == "div":
#         result = digit1 / digit2
#         print(result)
