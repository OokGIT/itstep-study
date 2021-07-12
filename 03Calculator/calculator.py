# импортируем функции
from _functions import externalCommands, calc_operator, numeric_inp1

# Требуем ввести первое число и, вызывая функцию calc_operator, производим операции над числами, по ходу требуя ввечти ещё число...

chislo=numeric_inp1()

while True:
    operator = calc_operator()
    if operator == "add":
        chislo += numeric_inp1()
        print(chislo)
    elif operator == "minus":
        chislo -= numeric_inp1()
        print(chislo)
    elif operator == "multi":
        chislo *= numeric_inp1()
        print(chislo)
    elif operator == "div":
        try:
            chislo /= numeric_inp1()
        except ZeroDivisionError as e:
            print("На 0 делить нельзя -", e)
        print(chislo)
    elif operator == "exit":
        print("Спасибо! До новых встреч!..")
        exit()
    elif operator == "clean":
        print ("Память калькулятора очищена")
        chislo = numeric_inp1()
        print(chislo)
