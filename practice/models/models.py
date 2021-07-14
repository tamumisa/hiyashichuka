#テーブルのカラム情報を定義するためのクラスを格納します。
#テーブル操作を行う際のレコード生成もこのクラスを通して行います。
#カラム構成
#ID(int:キー情報)
#title(String)(128)お願いのタイトル)
#body(text:お願いの内容)
#date(datetime:お願いの投稿日時)

from sqlalchemy import Column,Integer,String,Text,DateTime
from models.database import Base
from datetime import datetime

#カラム情報の定義を行う
#テーブル名とカラム別にカラム名と方を使用しています
#ここで引数に渡しているBaseは次のdatebase.pyで作るインスタンスなので後で説明らしい（笑）
class Onegaicontent(Base):
    __tablename__ = "onegaicontents"
    id = Column(String(128),unique=True)
    body = Column(Text)
    date = Column(Datetime,default=datetime.now())

    def __init__(self,title=None,body=None,date=None):
        self.title = title
        self.body = body
        self.date = date

    def __repr__(self):
        return '<Title %r>' %(self.title)
