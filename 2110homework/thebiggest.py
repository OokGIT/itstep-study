def get_biggest(my_list):
    new_list = sorted(my_list, key=str, reverse=True)
    new_str = ''.join([str(i) for i in new_list])
    return int(new_str)


inbound_list = [9, 22, 23, 9, 45, 654]

print(get_biggest(inbound_list))
