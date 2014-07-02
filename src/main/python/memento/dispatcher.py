from flask import Flask, render_template, request
from memento.service import FlashcardController

memento = Flask(__name__)


@memento.route('/')
def main():
    return render_template('index.html')


@memento.route('/flashcard', methods=['GET'])
def falshcard():
    return render_template('add_flashcard.html')


@memento.route('/flashcard', methods=['POST'])
def add_flashcard():
    print(request)
    FlashcardController().save(request.form)
    return 'saved!'
