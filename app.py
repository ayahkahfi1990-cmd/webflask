from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/labirin')
def labirin():
    return render_template('labirin.html')

@app.route('/snake')
def snake():
    return render_template('snake.html')

@app.route('/bintang')
def bintang():
    return render_template('bintang.html')

@app.route('/luckyspin')
def luckyspin():
    return render_template('luckyspin.html')

@app.route('/tebakwarna')
def tebakwarna():
    return render_template('tebakwarna.html')

@app.route('/balapan')
def balapan():
    return render_template('balapan.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
