from pyassert import assert_that
from mongoengine import connect

from memento.flashcard.repository import FlashcardRepository


class TestFlashcardRepository:

    def test_given_existing_inactive_databe_create_new_connection(self):
        # given
        invactive_db = FlashcardRepository.create('inactive').database
        invactive_db.close()

        # when
        active_db = FlashcardRepository.create('active').database

        # then
        assert_that(invactive_db).is_not_equal_to(active_db)

    def teardown_class():
        connection = connect('clear')

        for database_name in connection.database_names():
            connection.drop_database(database_name)
