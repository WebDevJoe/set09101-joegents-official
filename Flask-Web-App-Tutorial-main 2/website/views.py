from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

# Code from https://www.youtube.com/watch?v=dam0GPOAvVI&t=4299s
views = Blueprint('views', __name__)


# Define notes globally
notes = []

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)
    # Code from https://www.youtube.com/watch?v=dam0GPOAvVI&t=4299s


    #code from https://www.youtube.com/watch?v=31sSJjMoyw8

@views.route('/image-search')
def image_search():
    return render_template('image-search.html', user=current_user)

@views.route('/sticky')
def sticky():
    load_notes()
    return render_template('sticky-notes.html', user=current_user, notes=notes)

@views.route('/add_note', methods=['POST'])
def add_note():
    note_text = request.form['note_text']
    note_colour = request.form['note_colour']
    notes.append({'text': note_text, 'colour': note_colour})
    save_notes()
    return sticky()

# code from https://www.youtube.com/watch?v=31sSJjMoyw8
@views.route('/delete_note/<int:note_id>', methods=['GET', 'POST'])
def delete_note(note_id):
    if request.method == 'POST':
        if 0 <= note_id < len(notes):
            del notes[note_id]
            save_notes()
        return sticky()


# code from https://www.youtube.com/watch?v=31sSJjMoyw8
def load_notes():
    global notes
    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []

# code from https://www.youtube.com/watch?v=31sSJjMoyw8
def save_notes():
    with open('notes.json', 'w') as file:
        json.dump(notes, file, indent=4)


