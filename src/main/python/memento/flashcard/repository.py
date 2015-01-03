from collections import namedtuple
from mongoengine import ValidationError

from memento.flashcard.document import FlashcardDocument


Flashcard = namedtuple('Flashcard', ['ident', 'problem', 'solution'])


class FlashcardRepository:

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
