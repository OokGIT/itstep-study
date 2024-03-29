import re
my_text = 'Вот вы и закончили это упражнение! Оно может показаться сложным в ' \
          'зависимости от вашего уровня знания компьютера. Если вы сталкиваетесь ' \
          'с трудностями при выполнении этого упражнения, потратьте время на ' \
          'тренировку и выполнение описанных действий. Ведь если вы не умеете делать ' \
          'эти базовые операции, вам будет очень сложно при настоящем программировании ' \
          'в будущих упражнениях. Если программисты советуют использовать программу ' \
          'vim или emacs, откажитесь. Эти редакторы будут уместны, когда вы достигнете ' \
          'более высокого уровня программирования. Все, что вам нужно сейчас, — ' \
          'программа, которая позволяет помещать текст в файл. Я рекомендую использовать ' \
          'текстовый редактор gedit, TextWrangler или Notepad ++, потому они просты и ' \
          'работают схожим образом на всех компьютерах. Профессиональные программисты тоже ' \
          'используют эти текстовые редакторы.'

my_keyword = 'вы'


def get_annotations(get_text, get_word):
    # annotation = [i for i in text('. ') if word in i]
    # return annotation
    sentences = re.split(r' *[\.\?!][\'"\)\]]* * ', get_text)
    print(sentences)
    annotations = [i for i in sentences if get_word in i]
    return annotations
    # return sentences


print(get_annotations(my_text, my_keyword))
