def sum_digits(my_string):
    total = 0
    my_sum = '0'
    for i in my_string:
        if i.isdigit():
            my_sum += i
        else:
            total += int(my_sum)
            my_sum = '0'
    return total + int(my_sum)


print(sum_digits('sdfsdfs878sdfsdfsdf55sdfsdfsd09'))
