from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Selamat Datang!</h1>
    <h2>Website Flask Pertama Saya</h2>
    <p>Website ini online menggunakan Render.</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
