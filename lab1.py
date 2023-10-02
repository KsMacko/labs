print("Task 1:")
s = int(input("Enter the amount of seconds: "))
days = s // 86400
hours = s % 86400 // 3600
minutes = s % 86400 % 3600 // 60
seconds = s % 86400 % 3600 % 60
print("Days: ", days, "Hours: ", hours, "Minutes: ", minutes, "Seconds:", seconds)
print("\nTask 2:")
s = input("Please, enter the string: ")
for i in s:
    if i.isdigit():
        print(i)
print("\nTask 3:")
lis = ["Python", 15442, 32, "QweRty", 34, 19, "love"]
vowel = "aeyuio"
vowels = 0
consonant = 0
for i in lis:
    if type(i) is str:
        for letter in i:
            letter = letter.lower()
            if letter in vowel:
                vowels += 1
            else:
                consonant += 1
        print("Word - ", i, "Vowels - ", vowels, "Consonants - ", consonant)
        vowels = 0
        consonant = 0
print("\nTask 4:")
dict1 = {"a": 11, "c": 2}
dict2 = {"b": 11, "a": 13, "e": 30}
dict3 = {"f": 77}
print("        ~Method 1")
dict1.update(dict2)
dict1.update(dict3)
print(dict1)
print("        ~Method 2 (Sum of the values from similar keys)")
for k, v in dict2.items():
    if k not in dict1:
        dict1[k] = v
for k, v in dict3.items():
    if k not in dict1:
        dict1[k] = v
print(dict1)


print("\nTask 5:")
session = True


def view(c, jew):
    for j, value in jew.items():
        if c < 4:
            print(f"{j} -  {value[c - 1]}")
        else:
            print(f"{j} -  Материал: {value[0]} | Цена: {value[1]} | Количество: {value[2]}\n")


def buy_product(n, am, jew):
    if n in jew:
        price = jew[n][1]
        if am <= jew[n][2]:
            total_price = price * am
            jew[n][2] -= am
            print(f"Вы приобрели {am} шт. {n} за {total_price} BYN")
        else:
            print(f"Извините, на складе недостаточно {n}!")
    else:
        print("Извините, товар не найден.")


jewerly = {"часы": ["Золото, серебро", 105, 6], "серьги": ["Золото, рубин", 235, 11],
           "подвеска": ["Серебро, фианит", 105, 6], "браслет": ["Серебро, хрусталь", 91, 9],
           "запонки": ["Серебро, сапфир, фианит", 326, 15], "колье": ["Золото, агат", 3139, 11],
           "бусы": ["Жемчуг, фианит", 366, 17], "брошь": ["Жемчуг, топаз,", 1441, 7]}
while session:
    choice = int(input(
        "1. Просмотр описания: название – описание\n2. Просмотр цены: название – цена\n3. Просмотр количества: "
        "название – количество\n4. Всю информацию\n5. Покупка\nЛюбое другое значение - Выход\n"))
    if choice < 5:
        view(choice, jewerly)
    elif choice == 5:
        name = input("Введите название: ")
        name = name.lower()
        amount = int(input("Введите количество: "))
        buy_product(name, amount, jewerly)
    else:
        print("До свидания!")
        session = False

print("\nTask 6:")
tuple1 = (1, 2, 3, -5, 10)
summ = 0
for i in tuple1:
    if i >= 0:
        sum += i
    else:
        break

print(summ)

