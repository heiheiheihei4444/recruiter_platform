from app.extend import db

class BaseModel(db.Model):
    __abstract__=True
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            print(a)
            return False

class Goods(BaseModel):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    g_name=db.Column(db.String(16))
    g_price=db.Column(db.Float,default=0)