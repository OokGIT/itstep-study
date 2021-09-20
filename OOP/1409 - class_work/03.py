def compare_lists(list1, list2):
    my_list1 = set(list1)
    my_list2 = set(list2)
    compare = my_list1 - my_list2
    print(compare)


compare_lists([1, 3, 4], [2, 4, 5])
compare_lists([1, 2, 3], [2, 4, 5])
