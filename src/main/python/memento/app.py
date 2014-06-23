from flask import Flask, render_template

memento = Flask(__name__)


@memento.route('/')
def main():
    return render_template('index.html')


@memento.route('/flashcard', methods=['GET', 'POST'])
def add_falshcard():
    return render_template('flashcard_form.html')
