from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Plant(db.Model):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String)
    price = db.Column(db.Numeric(precision=10, scale=2))