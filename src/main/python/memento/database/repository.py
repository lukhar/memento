from memento.database.document import FlashcardDocument
from collections import namedtuple


Flashcard = namedtuple('Flashcard', ['ident', 'problem', 'solution'])


class FlashcardRepository:

    def add(self, flashcard):
        FlashcardDocument(problem=flashcard.problem,
                          solution=flashcard.solution).save()
