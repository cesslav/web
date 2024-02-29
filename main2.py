from flask import Flask, url_for
import requests

app = Flask(__name__)


@app.route('/')
def mission_name():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def mission_slogan():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promo():
    return """<!doctype html>
                <html lang="en">
                  <body>
                    <h1>Человечество вырастает из детства.</h1>
                    <h1>Человечеству мала одна планета.<h1>
                    <h1>Мы сделаем обитаемыми безжизненные пока планеты.<h1>
                    <h1>И начнем с Марса!<h1>
                    <h1>Присоединяйся!<h1>
                  </body>
                </html>"""


@app.route('/image_mars')
def image_mars():
    return """<!doctype html>
                <html lang="en">
                  <body>
                    <h1>Привет, Марс!</h1>
                    <h2>Жди нас, Марс!</h2>
                    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Mars_Valles_Marineris_EDIT.jpg/274px-Mars_Valles_Marineris_EDIT.jpg" alt="Здесь должен был быть марс, но я его не придумал.">
                    <p>Изображение Марса, великолепной красной планеты.</p>
                  </body>
                </html>"""


@app.route('/promotion_image')
def promo_image():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
                    <link rel="stylesheet" href="/static/css/style.css">
                  </head>
                  <body>
                    <div class="container">
                      <div class="row">
                        <div class="col">
                          <h1>Привет, Марс!</h1>
                          <h2>Жди нас, Марс!</h2>
                          <img src=https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Mars_Valles_Marineris_EDIT.jpg/274px-Mars_Valles_Marineris_EDIT.jpg" alt="Здесь должен был быть марс, но я его не придумал.">
                          <p>Изображение Марса, великолепной красной планеты.</p>
                        </div>
                      </div>
                    </div>
                  </body>
                </html>"""


@app.route('/promotion_mars')
def imagination():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">

                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Марс!</title>
                    </head>
                    <body>
                        <h1>Жди нас, Марс!</h1>
                        <img https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Mars_Valles_Marineris_EDIT.jpg/274px-Mars_Valles_Marineris_EDIT.jpg" alt="Здесь должен был быть марс, но я его не придумал.">

                    <div class="alert alert-dark" role="alert">
                     "Человечество вырастает из детства."
                     </div>

                    <div class="alert alert-primary" role="alert">
                    "Человечеству мала одна планета."
                    </div>

                    <div class="alert alert-danger" role="alert">
                    "Мы сделаем обитаемыми безжизненные пока планеты."
                    </div>

                    <div class="alert alert-warning" role="alert">
                    И начнем с Марса!
                    </div>

                    <div class="alert alert-primary" role="alert">
                    "Присоединяйся!
                    </div>

                           </body>
                         </html>
                         '''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if requests.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/form.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h2 align="center">Анкета претендента</h1>
                            <h3 align="center"> на участие в миссии</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="username" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите имя" name="username">
                                    <input type="secondusername" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите фамилию" name="secondname">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="email" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Высшее</option>
                                          <option>Среднее</option>
                                          <option>Среднее специальное</option>
                                        </select>
                                     </div>
                                     <label for="classSelect">Какое у вас образование?</label>
                                     <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">инженер-исследователь </label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">пилот </label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">строитель </label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">экзобиолог </label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">врач </label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">климатолог </label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">специалист по радиационной защите </label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">метеоролог </label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">оператор марсохода </label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">киберинженер </label>

                                    </div><div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">штурман </label>

                                    </div><div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">пилот дронов </label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">гляциолог </label>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в нашей миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе? </label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif requests.method == 'POST':
        print(requests.form['email'])
        print(requests.form['password'])
        print(requests.form['class'])
        print(requests.form['file'])
        print(requests.form['about'])
        print(requests.form['accept'])
        print(requests.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(debug=True)