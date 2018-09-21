import os
from glob import glob


CUR_DIR = os.path.dirname(__file__)
DATA_FOLDER = os.path.join(CUR_DIR, 'data')


def _get_note_path(note_name: str):
    return os.path.join(DATA_FOLDER, '%s.txt' % note_name)


def create_note(note_name: str, content=''):
    note_path = _get_note_path(note_name)

    with open(note_path, 'w') as note:
        note.write(content)

    if os.path.isfile(note_path):
        print('La note %s à bien été créée.' % note_name)


def delete_note(note_name: str):
    note_path = _get_note_path(note_name)

    if os.path.isfile(note_path):
        os.remove(note_path)
        print('La note %s à bien été supprimée.' % note_name)
    else:
        print('La note %s n\'existe pas.' % note_name)


def get_notes():
    notes = glob('%s/*.txt' % DATA_FOLDER)
    return [os.path.splitext(os.path.split(note)[-1])[0] for note in notes]
