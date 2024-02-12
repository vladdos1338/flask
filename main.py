from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def page():
    return 'Миссия колонизации марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблоки цвести'


@app.route('/promotion')
def promotion():
    pf_list = [
        'Человечество вырастает из детства.',
        'Человечеству мала одна планета.',
        'Мы сделаем обитаемыми безжизненные пока планеты.',
        'И начнем с Марса!',
        'Присоединяйся!'
    ]
    return "<br>".join(pf_list)


@app.route('/image_mars')
def img_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}" 
           alt="здесь должна была быть картинка, но не нашлась"
           <p>Вот она какая, красная планета.</p>
                  </body>
                </html>"""


@app.route('/promotion_image')
def promotion_image():
    pf_list = [
        'Человечество вырастает из детства.',
        'Человечеству мала одна планета.',
        'Мы сделаем обитаемыми безжизненные пока планеты.',
        'И начнем с Марса!',
        'Присоединяйся!'
    ]
    url_pic = url_for('static', filename='img/mars.gif')
    url_style = url_for('static', filename='css/style.css')
    return """<!doctype html>
            <html lang="en">
              <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <link rel="stylesheet" 
                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                crossorigin="anonymous">
                <link rel="stylesheet" type="text/css" href="{}" />
                <title>Колонизация</title>
              </head>
              <body>
                <h1>Жди нас, Марс</h1>
                <img src="{}" 
                alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert-dark" role="alert">
                      <br><h2>{}</h2>
                    </div>
                    <div class="alert-success" role="alert">
                      <br><h2>{}</h2>
                    </div>
                    <div class="alert-secondary" role="alert">
                      <br><h2>{}</h2>
                    </div>
                    <div class="alert-danger" role="alert">
                      <br><h2>{}</h2>
                    </div>
                    <div class="alert-warning" role="alert">
                      <br><h2>{}</h2>
                    </div>
                  </body>
                </html>
                """.format(url_style, url_pic, *pf_list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
