            # Пароль

correct_password = "password123" 
user_input = input("Введіть пароль: ")
if user_input == correct_password:
    print("Ви увійшли в систему")
else:
    print("Неправильний пароль")

            # Дні тижня

day_number = int(input("Введіть номер дня тижня (1-7): "))
days_of_week = {
    1: "Понеділок",
    2: "Вівторок",
    3: "Середа",
    4: "Четвер",
    5: "П'ятниця",
    6: "Субота",
    7: "Неділя"
}
if 1 <= day_number <= 7:
    print("Це", days_of_week[day_number])
else:
    print("Помилка: введено некоректний номер дня!")

            # Таблиця множення

num = int(input("Введіть число для таблиці множення: "))
print(f"Таблиця множення для {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

            # Сума чисел

numbers = [100, 2000, 230, 570, 500]
total_sum = sum(numbers)
print("Список чисел:", numbers)
print("Сума чисел:", total_sum)

            # Факторіал числа

num = int(input("Введіть число для обчислення факторіала: "))
if num < 0:
    print("Факторіал визначається тільки для невід'ємних чисел!")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"Факторіал числа {num} = {factorial}")

            # Парні числа

even_numbers = [num for num in range(1, 51) if num % 2 == 0]
print("Парні числа від 1 до 50:", even_numbers)

            # Пошук простих чисел

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

start = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінець діапазону: "))

prime_numbers = [num for num in range(start, end + 1) if is_prime(num)]

print(f"Прості числа в діапазоні від {start} до {end}: {prime_numbers}")

            # Робота із списками

numbers = [1, 2, 3, 4, 5]

numbers.append(10)
numbers.append(20)

numbers.remove(10)

print("Оновлений список чисел:", numbers)

            # Знаходження суми

numbers = [50, 10, 15, 25, 250]

total_sum = sum(numbers)

print("Список чисел:", numbers)
print("Сума всіх чисел у списку:", total_sum)

            # Подвійні значення

numbers = [3, 4, 7, 8, 12]

doubled_numbers = [num * 2 for num in numbers]

print("Оригінальний список чисел:", numbers)
print("Подвоєний список чисел:", doubled_numbers)

            # Робота із кортежами

fruits = ("яблуко", "банан", "апельсин")

print("Перший елемент:", fruits[0])
print("Другий елемент:", fruits[1])
print("Третій елемент:", fruits[2])

            # Об'єднання кортежів

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

merged_tuple = tuple1 + tuple2

print("Об'єднаний кортеж:", merged_tuple)

            # Робота із словниками

athlete_info = {
    "ім'я": "Поль Погба",
    "вік": 32,
    "спорт": "Футбол",
    "команда": "Ювентус",
    "країна": "Франція"
}

print("Інформація про спортсмена:")
for key, value in athlete_info.items():
    print(f"{key}: {value}")

            # Оновлення словника

favorite_books = {
    "1984": 1949,
    "Гаррі Поттер і філософський камінь": 1997,
    "Великий Гетсбі": 1925
}

favorite_books["Мобі Дік"] = 1851

print("Оновлений словник з улюбленими книгами:")
for title, year in favorite_books.items():
    print(f"Назва книги: {title}, Рік видання: {year}")

            # Пошук значення

countries_and_capitals = {
    "Україна": "Київ",
    "Франція": "Париж",
    "Німеччина": "Берлін",
    "Італія": "Рим",
    "США": "Вашингтон",
    "Японія": "Токіо"
}

country = input("Введіть назву країни: ")

if country in countries_and_capitals:
    print(f"Столиця {country}: {countries_and_capitals[country]}")
else:
    print("Ця країна не знайдена в словнику.")