#flaskとrender_template(HTMLを表示させるための関数)をインポート
from flask import Flask,render_template,request
#クエリストリングを受け取ってhtmlに送る

#flaskオブジェクトの生成
app = Flask(__name__)

#.[/]へアクセスがあった場合に、"HELLO KITTY"の文字列を返す
@app.route('/')
def hello():
    return "HELLO KITTY(=^・^=)"

#.[/index]へアクセスがあった場合に、「index.html」を返す
@app.route('/index')
def index():
    #requestモジュールをインポートして、以下の文でクエリストリングを受け取ることが出来る
    name = request.args.get("name")
    guzai = ["きゅうり","たまご","ハム","トマト"]
    return render_template("index.html",name=name,guzai=guzai)

@app.route('/index',methods=["POST"])
def post():
    name=request.form["name"]
    guzai = ["きゅうり","たまご","ハム","トマト"]
    return render_template("index.html",name=name,guzai=guzai)

#おまじない
if __name__ == '__main__':
    app.run(debug=True)