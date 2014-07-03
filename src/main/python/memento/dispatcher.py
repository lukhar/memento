from flask import Flask, render_template, request
from memento.service import FlashcardController

memento = Flask(__name__)


@memento.route('/')
def main():
    return render_template('index.html')


@memento.route('/flashcard/new', methods=['GET'])
def flashcard_form():
    return render_template('new_flashcard_form.html')


@memento.route('/flashcard', methods=['POST'])
def add_flashcard():
    FlashcardController().save(request.form)
    return 'saved!'
