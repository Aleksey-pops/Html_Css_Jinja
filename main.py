from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    with open('file.txt', 'r', encoding='utf =8') as file:
        resultData = list()
        for line in file.readlines():
            resultData.append(tuple(line.split('\n')[0].split(";")))
    return render_template('base.html', data=resultData)


@app.route('/about')
def about():
    return render_template('about.html')


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
