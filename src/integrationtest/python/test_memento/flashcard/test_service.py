from pyassert import assert_that
from nose_parameterized import parameterized

from memento.flashcard.repository import FlashcardRepository, Flashcard
from memento.flashcard.service import FlashcardService
from memento.flashcard.document import database


class TestFalshcardService:

    def setup(self):
        self.repository = FlashcardRepository()
        self.service = FlashcardService(self.repository)

    def teardown_class():
        database.drop_database('memento')

    def test_given_valid_flashcard_data_create_new_flashcard_in_repository(self):
        # given
        flashcard_data = {'problem': 'What is 2 + 2?',
                          'solution': '2 + 2 = 4'}

        # when
        flashcard_id = self.service.post(flashcard_data)

        # then
        assert_that(self.repository.get(flashcard_id)).is_equal_to(
            Flashcard(str(flashcard_id),
                      flashcard_data['problem'],
                      flashcard_data['solution']))

    def test_given_existing_flashcard_id_retrieve_flashcard(self):
        # given
        exiting_flashcard_data = {'problem': 'What is the name of first Polish king?',
                                  'solution': 'Boleslaw Chrobry'}
        existing_id = self.service.post(exiting_flashcard_data)

        # when
        flashcard = self.service.get(existing_id)

        # then
        assert_that(flashcard).is_equal_to(
            Flashcard(str(existing_id),
                      exiting_flashcard_data['problem'],
                      exiting_flashcard_data['solution']))

    def test_given_not_existing_flashcard_id_raise_validation_exception(self):
        # given
        valid_non_existing_id = '14a6753f6e2b77acac0d2cc1'

        # when
        flashcard = self.service.get(valid_non_existing_id)

        # then
        assert_that(flashcard).is_none()

    @parameterized([
        'tooshort',
        'toolong111111111111111122222222',
        'InvalidCharacters!@$%^&*',
    ])
    def test_given_invalid_flashcard_id_return_nothing(self, invalid_id):
        # when
        flashcard = self.service.get(invalid_id)

        # then
        assert_that(flashcard).is_none()
