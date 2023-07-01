from flask import Flask

app = Flask(__name__)

#www.cursodepython.com/

@app.route("/")
def hello_world():
    return "<p>Hello, world!</p>"

'''
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
'''

#Executa o aplicativo
if __name__ == '__main__':
    app.run()



