import csv
import random
with open("books.csv") as r_file:

    file_reader = csv.DictReader(r_file, delimiter = ";")
    books = []
    count = 0
    k = 0
    k1 = 0
    s0 = input('Введите автора.')

    for row in file_reader:
        count += 1
        books.append(row)
        name = row['Название']
        date = row['Дата поступления']
        avt = row['Автор']
        if len(name)>30:
            k +=1

        d=int(date[8:10])
        if d > 17 and avt == s0:
            k1 +=1
            print(f'Книги { s0 } от 2018 года: {name}')

    print(f'В файле { count } записей.')
    print(f'В файле { k } записей имеют название книги длиной более 30 символов.')
    if k1 < 1:
        print('Такой книги не найдено.')

    with open("test.txt", "w") as myfile:
        for i in range(20):
            num = random.randint(1, count)
            s = books[num]
            a = s['Автор']
            n = s['Название']
            d = s['Дата поступления']
            myfile.write(f'{num}. {a}. {n} - {d[6:10]} \n')