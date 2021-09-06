import time


# Функция-декоратор для оперделения времени выполнения основной функции
def exe_time(func):
    def timing(*args):
        start = time.perf_counter_ns()
        res = func(*args)
        print("Время выполнения, нс:", time.perf_counter_ns() - start)
        return res
    return timing


# @exe_time
# Рисуем строку длины l_l
def smb(_str, size):
    symbol = _str * size * 2
    return symbol


l_l = 10
l1 = smb('*', l_l)
l2 = smb('*', 1) + smb('#', l_l - 2) + smb('*', 1)
l3 = smb('*', 1) + smb('#', 1) + smb('%', l_l - 4) + smb('#', 1) + smb('*', 1)
l4 = smb('*', 1) + smb('#', 1) + smb('%', 1) + smb('^', l_l - 6) + \
     smb('%', 1) + smb('#', 1) + smb('*', 1)
l5 = smb('*', 1) + smb('#', 1) + smb('%', 1) + smb('^', 1) +\
     smb('@', l_l - 8) + smb('^', 1) + smb('%', 1) + smb('#', 1) + smb('*', 1)
draw_ascii = (l1, l2, l3, l4, l5, l4, l3, l2, l1)
# print(l1, l2, l3, l4, l5, l4, l3, l2, l1, sep="\n")
# print(list(draw_ascii))
with open('results.txt', 'w') as wrt:
    for i in draw_ascii:
        wrt.write(str(i) + '\n')
