from flask import Flask, render_template, request
from memento.service import FlashcardService

memento = Flask(__name__)


@memento.route('/')
def main():
    return render_template('index.html')


@memento.route('/flashcards/new', methods=['GET'])
def flashcard_form():
    return render_template('flashcard/new_form.html')


@memento.route('/flashcards', methods=['POST'])
def add_flashcard():
    ident = FlashcardService().post(request.form)
    return 'saved! {}'.format(ident)


@memento.route('/flashcards/<ident>', methods=['GET'])
def get_flashcard(ident):
    flashcard = FlashcardService().get(ident)
    return render_template('flashcard/display.html', flashcard=flashcard)
