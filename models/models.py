from sqlalchemy import Column, Integer, String, Text, DateTime
from models.database import Base
from datetime import datetime

class OnegaiContent(Base):
    __tablename__ = 'onegaicontents'
    id = Column(Integer, primary_key=True)
    title = Column(String(128), unique=True)
    body = Column(Text)
    date = Column(DateTime, default=datetime.now())

    def __init__(self, title=None, body=None, date=None):
        self.title = title
        self.body = body
        self.date = date
    
    def __repr__(self):
        return '<Title %r>' % (self.title)
        # %rは文字列として出力される
        # __repr__はモデルクラスの定義で書かなくちゃいけないらしい？？
        # https://gene.hatenablog.com/entry/20151011/1444546659