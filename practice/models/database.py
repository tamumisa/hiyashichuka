#DBとの直接的な接続の方法を格納します

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

#DBへの接続情報を定義している
#①datebase.pyと同じパスに onegai.dbというファイルを絶対パスで定義
databese_file = os.path.join(os.path.abspath(os.path.dirname(__file__)),'onegai.db')
#②SQliteを利用して1.で定義した絶対パスにDBを構築
engine = create_engine('sqlite:///' + databese_file,convert_unicode=True)
#③DB接続用インスタンスを生成
db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))
#Baseオブジェクトを生成して
Base = declarative_base()
#そこにDBの情報を流し込む
Base.query = db_session.query_property()

#DB初期化のための関数を定義
def init_db():
    import models.models
    Base.metadate.create_all(bind=engine)
