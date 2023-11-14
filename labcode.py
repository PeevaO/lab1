import csv
import random
max_name = 30
min_year = 18
with open('books.csv') as file:

    file_reader = csv.DictReader(file, delimiter=';')
    books = []
    records_num = 0
    long_names_num = 0
    found_books = 0
    input_author = input('Введите автора.')

    for row in file_reader:
        records_num += 1
        books.append(row)
        name = row['Название']
        date = row['Дата поступления']
        author = row['Автор']
        if len(name) > max_name:
            long_names_num += 1

        year = int(date[8:10])
        if year >= min_year and author == input_author:
            found_books += 1
            print(f'Книги { input_author } от 2018 года: {name}')

    print(f'В файле { records_num } записей.')
    print(f'В файле { long_names_num } записей имеют название книги длиной более 30 символов.')
    if found_books < 1:
        print('Такой книги не найдено.')

    with open("test.txt", "w") as my_file:
        for i in range(20):
            num = random.randint(1, records_num)
            book_line = books[num]
            author = book_line['Автор']
            name = book_line['Название']
            date = book_line['Дата поступления']
            my_file.write(f'{num}. {author}. {name} - {date[6:10]} \n')
