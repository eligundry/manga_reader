import os

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.label import Label

from application.models import db, engine, Base
from config import SQLITE_DB_LOCATION

class MangaReader(App):
    def build(self):
        # Init the database
        if not os.path.exists(SQLITE_DB_LOCATION):
            Base.metadata.create_all(engine)

        return Label(text='Hello World')
