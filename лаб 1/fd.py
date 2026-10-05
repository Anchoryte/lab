def char_range(a, b):
    letters_set = set()
    letter = a
    while letter <= b:
        letters_set.add(letter)
        letter = chr(ord(letter) + 1)
    return letters_set

rus_letters = set().union({'Ё', 'ё'}, char_range('а', 'я'), char_range('А', 'Я'))
#print(sorted(rus_letters))

variants_number = 10

print('Введите фамилию: ')
name = input()
name = ''.join(letter.capitalize() for letter in name).replace('Ё', 'Е')

print('Ваша фамилия: ', name)

bad_letter = False
name_code = 0
for letter in name:
    if letter not in rus_letters:
        bad_letter = True
        break
    name_code += ord(letter)
if bad_letter:
    print("ОШИБКА: В строке должны быть только русские буквы")
else:
    variant = name_code % variants_number + 1
    print("Ваш вариант: ", variant)