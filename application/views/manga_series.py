from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

from application.models import db, MangaSeries

class MangaSeriesItemView(Button):

    def __init__(self, series, **kwargs):
        super().__init__(**kwargs)

        self.title = series.title

class MangaSeriesView(GridLayout):
    def __init__(self, **kwargs):
        # Setup the view
        super().__init__(**kwargs)

        q = db.query(MangaSeries).order_by(MangaSeries.title)

        # If there are no items currently in the DB, attempt to load them all
        if not q.count():
            MangaSeries.hydrate()

        series = q.all()

        for item in series:
            self.add_widget(MangaSeriesItemView(item))

        scroll_view = ScrollView()
        scroll_view.add_widget(self)

        return scroll_view
