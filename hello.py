from flask import Flask
app = Flask(__name__)
@app.route('/')
@app.route('/hello')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

@app.route('/contact-us')
def ContactUs():
    return "Contact Us Page"
# ИДИОМА, КОТОРАЯ ОБЕСПЕЧИВАЕТ ЗАПУСК СЦЕНАРИЯ ТОЛЬКО В СЛУЧАЕ, ЕСЛИ ОН ЗАПУСКАЕТСЯ НЕПОСРЕДСТВЕННО САМ СЦЕНАРИЙ, А
# НЕ ЕГО ИМПОРТ
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',
         port=9000,
         threaded=True)

# После запуска сервер входит в цикл ожидания и обработки запросов. Этот цикл продолжается, пока приложение не будет остановлено,
# например нажатием комбинации Ctrl-C.