#flaskとrender_template(HTMLを表示させるための関数)をインポート
from models.models import OnegaiContent
from flask import Flask,render_template, request
from models.models import OnegaiContent
from models.database import db_session
from datetime import datetime

#flaskオブジェクトの生成
app = Flask(__name__)

#.[/]へアクセスがあった場合に、"HELLO KITTY"の文字列を返す
"""
@app.route('/')
def hello():
    return "HELLO {name}(=^・^=)".format(name="tamu")
"""
#.[/index]へアクセスがあった場合に、「index.html」を返す

@app.route('/index')
def index():
    name = request.args.get("name")
    okyo = ["色不異空","空不異色","色即是空","空即是色"]
    return render_template("index.html", name=name, okyo=okyo)

@app.route('/')
@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/login', methods=["post"])
def to_login():
    name = request.form["name"]
    all_onegai = OnegaiContent.query.all()
    return render_template("index.html", name=name, all_onegai=all_onegai)

@app.route('/add', methods=["post"])
def add():
    title = request.form["title"]
    body = request.form["body"]
    name = request.form["name"]
    content = OnegaiContent(title, body, datetime.now())
    db_session.add(content)
    db_session.commit()
    return index()



#おまじない
if __name__ == '__main__':
    app.run(debug=True)