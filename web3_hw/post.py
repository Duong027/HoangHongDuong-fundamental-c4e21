# lam viec voi database
from mongoengine import Document,StringField,IntField

class Post(Document):
    title = StringField()
    author = StringField()
    content = StringField()
    likes = IntField()

