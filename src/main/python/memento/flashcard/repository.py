from collections import namedtuple
from mongoengine import ValidationError, connect

from memento.flashcard.document import FlashcardDocument


Flashcard = namedtuple('Flashcard', ['ident', 'problem', 'solution'])


class FlashcardRepository:

    database = None

    def add(self, flashcard):
        flashcard = FlashcardDocument(problem=flashcard.problem,
                                      solution=flashcard.solution).save()

        return flashcard.id

    def get(self, ident):
        try:
            document = FlashcardDocument.objects(id=ident).first()
        except ValidationError:
            return None

        if document is None:
            return None

        return Flashcard(ident=str(document.id),
                         problem=document.problem,
                         solution=document.solution)

    @classmethod
    def create(cls, database_name='memento'):
        if cls.database is None or cls.database.alive() is False:
            cls.database = connect(database_name)

        return FlashcardRepository()
