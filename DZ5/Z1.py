# Напишите программу, удаляющую из 
# текста все слова содержащие "абв".

text = 'Привет абв как дела абв убрать все буквы абв'

def del_words(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

text = del_words(text)
print(text)