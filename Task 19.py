#todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
# id) - номер по порядку (от 1 до 10);
# значение из списка algoritm
# algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" ,
#             "Apriori", "EM", "PageRank" , "AdaBoost", "kNN" ,
#             "Наивный байесовский классификатор", "CART" ]
# Каждое значение из списка должно находится на отдельной строке.
# Пример файла algoritm.csv:
# 1) "C4.5"
# 2) "k - means"

import csv




id_w = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
algoritm: list[str] = [ "C4.5", "k - means", "Метод опорных векторов",
             "Apriori", "EM", "PageRank", "AdaBoost", "kNN",
             "Наивный байесовский классификатор", "CART" ]

f = open("Task19algoritm.csv", "w+")
with f:
    writer = csv.writer(f)
    for line in range(1, 11):
        writer.writerow([line,algoritm[line-1]])

f.close()




