word = input("Введіть слово: ")
p = word[-1]
count = 0
for char in word:
    if char == p:
        count += 1

print("Кількість співпадінь в слові:", count)
