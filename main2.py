from flask import Flask, url_for, request, render_template

app = Flask(__name__)


def main():
    if __name__ == '__main__':
        app.run(port=8080, host='127.0.0.1')


@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['username'] = "Ученик Яндекс.Лицея"
    param['title'] = 'Домашняя страница'
    return render_template('index.html', **param)


@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number_1=2, number_2=11)


main()
