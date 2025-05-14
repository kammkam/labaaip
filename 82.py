
points = {
    1: "АВЕИНОРСТ",
    2: "ДКЛМПУ",
    3: "БГЁЬЯ",
    4: "ЙЫ",
    5: "ЖЗХЦЧ",
    8: "ШЭЮ",
    10: "ФЩЪ"
}


letter_values = {}
for point, letters in points.items(): # возвращает все пары ключ знач из словаря
    for letter in letters:
        letter_values[letter] = point


word = input("Введите слово: ").upper()
total = 0

for letter in word:
    total += letter_values.get(letter, 0)

print(f"Стоимость слова «{word}»: {total} очков")



