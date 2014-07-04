from memento.database.repository import FlashcardRepository, Flashcard


class FlashcardController:

    def __init__(self, flashcardRepository=FlashcardRepository()):
        self.repository = flashcardRepository

    def save(self, args):
        flashcard = Flashcard(ident=None, problem=args['problem'], solution=args['solution'])
        self.repository.add(flashcard)
