from mongoengine import Document, StringField


class FlashcardDocument(Document):
    problem = StringField()
    solution = StringField()
