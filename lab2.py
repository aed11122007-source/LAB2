import csv
import xml.dom.minidom


# Выводит количество записей, у которых в поле Название строка длиннее 30 символов.
def line_str(books_csv):
    books_csv.seek(0)
    reader = csv.DictReader(books_csv, delimiter=";")
    kol_vo = [
        line["Цена поступления"] for line in reader if len(str(line["Название"])) > 30
    ]
    return len(kol_vo)


# Поиск книги по автор
def search(books_csv):
    print("Введи автора:")
    name = input()
    books_csv.seek(0)
    reader = csv.DictReader(books_csv, delimiter=";")
    recommendation = [
        line["Название"]
        for line in reader
        if line["Автор"] == f"{name}" and float(line["Цена поступления"]) > 200
    ]
    return recommendation


#  Генератор библиографических ссылок вида <автор>. <название> - <год> для 20 записей
def list_20(booksen_csv, booksen_txt):
    print("Напиши 20 любых позиций через пробел:")
    positions = input()
    positions_list = positions.split()
    reader = csv.DictReader(booksen_csv, delimiter=";")
    file = [line for line in reader]
    list = [
        str(int(i))
        + ". "
        + str(file[int(i) - 1]["Book-Author"])
        + ". "
        + str(file[int(i) - 1]["Book-Title"])
        + " - "
        + str(file[int(i) - 1]["Year-Of-Publication"])
        for i in positions_list
    ]
    for i in range(len(list)):
        booksen_txt.write(f"{list[i]}\n")
    return list


# Извлечение данных из xml-файла
def lists_2(dom):
    NumCode = []
    CharCode = []
    for node in dom.getElementsByTagName("NumCode"):
        NumCode.append(int(node.firstChild.data))
    for node in dom.getElementsByTagName("CharCode"):
        CharCode.append(node.firstChild.data)
    print(NumCode)
    print(CharCode)


if __name__ == "__main__":
    with open("books.csv") as books_csv:
        print(line_str(books_csv))
        print(search(books_csv))
    books_csv.closed()

    with open("books-en.csv") as booksen_csv:
        with open("booksen.txt", "w") as booksen_txt:
            print(list_20(booksen_csv, booksen_txt))
    booksen_txt.closed()
    booksen_csv.closed()

    dom = xml.dom.minidom.parse("currency.xml")
    print(lists_2(dom))
