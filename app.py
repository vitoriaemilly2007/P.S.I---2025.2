from flask import Flask
app = Flask(__name__)

@app.route('/')

def index():
    return 'Olá Mundooo'

@app.route('/contato')
def cotato():
    return 'alba.lops@ifrn.edu.br'

if __name__== '__main__':
    app.run()