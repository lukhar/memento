from memento.flashcard.repository import FlashcardRepository, Flashcard


class FlashcardService:

    def __init__(self, flashcard_repository=FlashcardRepository()):
        self.repository = flashcard_repository

    def post(self, args):
        flashcard = Flashcard(ident=None, problem=args['problem'], solution=args['solution'])
        return self.repository.add(flashcard)

    def get(self, ident):
        return self.repository.get(ident)
