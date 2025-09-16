from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def index():
    return 'Olá Mundooo'

@app.route('/contato')
def cotato():
    return '<h1>alba.lops@ifrn.edu.br<h1/>'
    
@app.route('/exemplo')
def exemplo():
    return render_template('exemplo.html')

@app.route('/exemplo2')
def exemplo2():
    return render_template('exemplo2.html')

if __name__== '__main__':
    app.run()