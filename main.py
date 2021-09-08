# new_file = open('text_file', 'w')
new_file = open('text_file', 'a')
# text = input('your text')
# new_file.write(f'{text}\n') я закоментувала, щоб не заважало, бо я вже текст ввела через інпут
new_file = open('text_file', 'r')

lines = 0
words = 0
letters = 0

for line in new_file:
    lines += 1
    letters += len(line)
    # прочитала про цікавий метод position in/out для розпізнання пробіл/нове слово вирішила спробувати, можливо можно було якось по-іншому
    pos = 'out'
    for letter in line:
        if letter != ' ' and pos == 'out':
            words += 1
            pos = 'in'
        elif letter == ' ':
            pos = 'out'
new_file.close()
print("Lines", lines)
print("Words", words)
print("Letters", letters)
