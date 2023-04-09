from flask import Flask, render_template
from random import randint as rd

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def main():
    name = rd(0, 1)
    return render_template('base.html', name=name)  # выводит код сразу на страницу


if __name__ == '__main__':
    app.run()

# file = open('file.txt', 'r')  # ОТКРЫВАЕМ ФАЙЛ
#
# list_1 = list() resultData = list() for line in file.readlines():  # выводит строку # print(line.split('\n')[
# 0].split(';'))  # разделяем строку через \n и через ';' resultData.append(tuple(line.split('\n')[0].split(';')))  #
# создаем кортеж (tuple) и записываем в результирующий список (append) # функция (append) добавляет элемент в конец
# списка print(file.read())  # считываем данные из файла и выводим # указывае к какому списку добавляем (resultData)
# и что добавляем file.close() print(resultData)
#
# '''
# a - режим добавления
# w -режим на запись (очишает файл)
# r - режим считывания
#
# '''
