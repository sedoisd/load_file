from flask import Flask, url_for, request
from PIL import Image
from io import BytesIO

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def choice():
    if request.method == 'GET':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />                        
                                <link rel="stylesheet" 
                                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                                crossorigin="anonymous">
                              </head>
                              <body>
                              <h1 align="center">Загрузка фотографии</h1>
                              <h3 align="center">для участия в миссии</h3>
                              <div>
                                <form class="login_form" method="post" enctype="multipart/form-data">
    
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                              </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        f = request.files.get('file')
        data = f.read()
        im = Image.open(BytesIO(data))
        # im.show()
        im.save('static/image/result.{im_format}'.format(im_format=im.format))
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />                        
                                <link rel="stylesheet" 
                                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                                crossorigin="anonymous">
                              </head>
                              <body>
                              <h1 align="center">Загрузка фотографии</h1>
                              <h3 align="center">для участия в миссии</h3>
                              <div>
                                <form class="login_form" method="post">
                                    <div class="form-group">
                                        <img src="{url_for('static', filename=f"image/result.{im.format}")}" 
                                           alt="здесь должна была быть картинка, но не нашлась">
                                    </div>
                                </form>
                              </div>
                              </body>
                            </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
