from memento.flashcard.document import FlashcardDocument
from collections import namedtuple


Flashcard = namedtuple('Flashcard', ['ident', 'problem', 'solution'])


class FlashcardRepository:

    def add(self, flashcard):
        flashcard = FlashcardDocument(problem=flashcard.problem,
                                      solution=flashcard.solution).save()

        return flashcard.id

    def get(self, ident):
        document = FlashcardDocument.objects(id=ident).first()

        if document is None:
            return None

        return Flashcard(ident=str(document.id),
                         problem=document.problem,
                         solution=document.solution)
