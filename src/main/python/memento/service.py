from memento.database import Flashcard


class FlashcardController:

    def save(self, args):
        Flashcard(problem=args['problem'], solution=args['solution']).save()
