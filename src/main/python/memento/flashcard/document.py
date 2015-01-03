from mongoengine import Document, StringField
from mongoengine import connect

database = connect('memento')


class FlashcardDocument(Document):
    problem = StringField()
    solution = StringField()
