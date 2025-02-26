from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
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
                            <title>Анкета на участие в отборе претендентов</title>
                          </head>
                          <body>
                            <h1 align="center">Анкета претендента</h1>
                            <h3 align="center">на участие в миссии</h3>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="surname" aria-describedby="emailHelp" placeholder="Введите фамилию" name="surname">
                                    <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <input type="email" class="form-control" id="email" placeholder="Введите почту" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="education">
                                          <option>Начальное</option>
                                          <option>Основное</option>
                                          <option>Среднее общее</option>
                                          <option>Среднее профессиональное</option>
                                          <option>Высшее</option>
                                        </select>
                                    </div>
                                    <div class="profession">
                                        <label for="form-check">Укажите вашу профессию</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="profession" id="pr1" value="инженер-исследователь" checked>
                                          <label class="form-check-label" for="pr">
                                            Инженер-исследователь
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="profession" id="pr2" value="Пилот">
                                          <label class="form-check-label" for="pr">
                                            Пилот
                                          </label>                                          
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="profession" id="pr3" value="Строитель">
                                          <label class="form-check-label" for="pr">
                                            Строитель
                                          </label>                                          
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="profession" id="pr4" value="Экзобиолог">
                                          <label class="form-check-label" for="pr">
                                            Экзобиолог
                                          </label>                                          
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="profession" id="pr5" value="врач">
                                          <label class="form-check-label" for="pr">
                                            Пилот
                                          </label>                                          
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="profession" id="pr6" value="инженер по терраформированию">
                                          <label class="form-check-label" for="pr">
                                            Инженер по терраформированию
                                          </label>                                          
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="profession" id="pr7" value="инженер жизнеобеспечения">
                                          <label class="form-check-label" for="pr">
                                            Инженер жизнеобеспечения
                                          </label>                                          
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="profession" id="pr7" value="климатолог">
                                          <label class="form-check-label" for="pr">
                                            Климатолог
                                          </label>                                          
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="profession" id="pr7" value="оператор марсохода">
                                          <label class="form-check-label" for="pr">
                                            Оператор марсохода
                                          </label>                                          
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="profession" id="pr7" value="киберинженер">
                                          <label class="form-check-label" for="pr">
                                            Киберинженер
                                          </label>                                          
                                        </div>
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
                                    <div class="form-group">
                                        <label for="motivation">Почему вы решили принять участие в миссии</label>
                                        <textarea class="form-control" id="motivation" rows="3" name="motivation"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов быть добровольцем</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        # print(request.form)
        print(f"Фамилия - {request.form.get('surname')}")
        print(f"Имя - {request.form.get('name')}")
        print(f"Почта - {request.form.get('email')}")
        print(f"Образование - {request.form.get('education')}")
        print(f"Профессия - {request.form.get('profession')}")
        print(f"Пол - {request.form.get('sex')}")
        print(f"Почему участвует - {request.form.get('motivation')}")
        print(f"Фото - {request.form.get('file')}")
        print(f"Остается - {request.form.get('accept')}")
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
