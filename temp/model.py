from datetime import datetime

from temp import db


# temp
class Temp(db.Model):
    __tablename__ = 'temp'

    temp = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='产品id')
    created_time = db.Column(db.DateTime, default=datetime.now, comment='创建时间')
    updated_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='更新时间')
