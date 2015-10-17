import os

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

from application.models import engine, Base
from application.views import MangaSeriesView
from config import SQLITE_DB_LOCATION

class MangaReader(App):
    def build(self):
        # Init the database
        Base.metadata.create_all(engine)

        return MangaSeriesView()
