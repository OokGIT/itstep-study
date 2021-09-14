n = ''
while n.isdigit() == False:
    n = str(int(input('Enter a number: ')))
# n = str(int(input()))
my_mult = 3
my_string = ''
my_result = 0
for i in range(1, my_mult + 1):
    my_string = n * i
    # print(my_string)
    # print(type(my_string))
    my_digit = float(my_string)
    my_result += my_digit

print(int(my_result))
