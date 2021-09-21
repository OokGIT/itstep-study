# 04 Найдите три ключа с самыми высокими значениями в словаре
# _dict = {'1key':123, '2key':9785, '3key': 560, '4key':234, '5key': 3451}.
_dict = {'1key': 123, '2key': 9785, '3key': 560, '4key': 234, '5key': 3451}
sorted_values = sorted(_dict.values())
res_list = sorted_values[-3:]
for k, v in _dict.items():
    if v in res_list:
        print(k)
