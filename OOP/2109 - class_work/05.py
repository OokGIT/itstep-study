my_string = 'Основным отличием Компьютерной'


# На выходе какой-то ключ - "sdf sd,sae;l,afs'df"
def encode_string(text):
    new_list = []
    temp_list = text.split()
    print(temp_list)
    for i in range(0, len(temp_list)):
        new_word = list(temp_list[i])
        for j in range(0, len(new_word)):
            enc_letter = ord(new_word[j])
            print(enc_letter, end="|")


# def decode (code, key):


encode_string(my_string)
