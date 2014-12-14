from nose.tools import assert_equal
from memento.flashcard.repository import FlashcardRepository, Flashcard
from memento.flashcard.service import FlashcardService


class TestFalshcardService:

    def setup(self):
        self.repository = FlashcardRepository()
        self.service = FlashcardService(self.repository)

    def test_given_valid_flashcard_add_it_to_repository(self):
        # given
        flashcard_data = {'problem': 'What is 2 + 2?',
                          'solution': '2 + 2 = 4'}

        # when
        flashcard_id = self.service.post(flashcard_data)

        # then
        assert_equal(self.repository.get(flashcard_id),
                     Flashcard(str(flashcard_id),
                               flashcard_data['problem'],
                               flashcard_data['solution']))
