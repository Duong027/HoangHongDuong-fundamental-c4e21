# lam viec voi database
from mongoengine import Document,StringField,IntField

class Post(Document):
    tendaydu = StringField()
    email = StringField()
    tendangnhap = StringField()
    matkhau = StringField()


