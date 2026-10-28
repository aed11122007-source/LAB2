import csv
import xml.dom.minidom

# def line_str(books_csv):
#     books_csv.seek(0)
#     reader = csv.DictReader(books_csv, delimiter = ';')
#     kol_vo = [line['Цена поступления'] for line in reader if\
#                   len(str(line['Название'])) > 30]
#     return len(kol_vo)

# def search(books_csv):
#     print('Введи автора:')
#     name = input()
#     books_csv.seek(0)
#     reader = csv.DictReader(books_csv, delimiter = ';')
#     recommendation = [line['Название'] for line in reader
#                       if line['Автор'] == f'{name}' 
#                       and float(line['Цена поступления']) > 200]
#     return recommendation


# def list_20(booksen_csv, booksen_txt):
#     print('Напиши 20 любых позиций через пробел:')
#     positions = input()
#     positions_list = positions.split()
#     reader = csv.DictReader(booksen_csv, delimiter=';')
#     file = [line for line in reader] 
#     list = [str(int(i)) + '. ' + 
#             str(file[int(i)-1]['Book-Author']) + '. ' +
#             str(file[int(i)-1]['Book-Title']) + ' - ' + 
#             str(file[int(i)-1]['Year-Of-Publication']) 
#             for i in positions_list]
#     for i in range(len(list)):
#         booksen_txt.write(f'{list[i]}\n')
#     return list



# def lists_2(currency_xml):
#     NumCode = []
#     CharCode = []
#     reader = csv.DictReader(currency_xml, delimiter=';')
        
#     return reader
    


# def lists_2(dom):
#     NumCode = []
#     CharCode = []
#     for node in dom.getElementsByTagName("NumCode"):
#         NumCode.append(int(node.firstChild.data))
#     for node in dom.getElementsByTagName("CharCode"):
#         CharCode.append(node.firstChild.data)
#     print(NumCode)
#     print(CharCode)

def popular(books_csv):
    name = input()
    books_csv.seek(0)
    reader = csv.DictReader(books_csv, delimiter = ';')
    top_20 = [int(line['Downloads']) for line in reader].sort()
    recommendation = [line['Book-Title'] for line in reader
                      if int(line['Downloads']) in top_20[-20:]]
    return recommendation

if __name__ == '__main__':
    # with open('books.csv') as books_csv:
    #     # print(line_str(books_csv))
    #     # print(search(books_csv)) 
    # books_csv.closed()

    # with open('books-en.csv') as booksen_csv:
    #    with open('booksen.txt', 'w') as booksen_txt:
    #        print(list_20(booksen_csv, booksen_txt))
    # booksen_txt.closed()
    # booksen_csv.closed()
    
    # dom = xml.dom.minidom.parse("currency.xml")
    # print(lists_2(dom))

    with open('books.csv') as booksen_csv:
            print(popular(booksen_csv))
    booksen_csv.closed()




