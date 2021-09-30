def get_bigger_list(input_list, my_digit):
    new_list = [i for i in input_list if i > my_digit]
    print(new_list)


a = [1, 2, 2, 23, 234234, 23, 4]
n = 5
get_bigger_list(a, n)
