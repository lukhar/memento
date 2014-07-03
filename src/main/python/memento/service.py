from memento.database.document import FlashcardDocument


class FlashcardController:

    def save(self, args):
        FlashcardDocument(problem=args['problem'], solution=args['solution']).save()
