#flaskとrender_template(HTMLを表示させるための関数)をインポート
from flask import Flask,render_template

#flaskオブジェクトの生成
app = Flask(__name__)

#.[/]へアクセスがあった場合に、"HELLO KITTY"の文字列を返す
@app.route('/')
def hello():
    return "HELLO KITTY(=^・^=)"

#.[/index]へアクセスがあった場合に、「index.html」を返す
@app.route('/index')
def index():
    return render_template("index.html")

#おまじない
if __name__ == '__main__':
    app.run(debug=True)