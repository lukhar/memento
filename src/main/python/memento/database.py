from mongoengine import Document, StringField
from mongoengine import connect

connect('memento_db')


class Flashcard(Document):
    problem = StringField()
    solution = StringField()
