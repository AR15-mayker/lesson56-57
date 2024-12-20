N = int(input("Введите количество футболистов: "))
count = 0
for _ in range(N):

    data = input("Введите данные футболиста в формате 'Фамилия Имя год_рождения голы': ")
    surname, name, birth_year, goals = data.split()


    birth_year = int(birth_year)
    goals = int(goals)


    if 1998 <= birth_year <= 2000 and goals == 0:
        count += 1

print(f"Количество футболистов, родившихся с 1998 по 2000 г., не забивших ни одного гола: {count}")