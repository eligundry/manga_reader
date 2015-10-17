from kivy.uix.gridlayout import GridLayout
from kivy.uix.listview import ListView

from application.models import db, MangaSeries

class MangaSeriesView(GridLayout):

    def __init__(self, **kwargs):
        # Setup the view
        kwargs['cols'] = 1
        super().__init__(**kwargs)

        q = db.query(MangaSeries).order_by(MangaSeries.title)

        # If there are no items currently in the DB, attempt to load them all
        if not q.count():
            MangaSeries.hydrate()

        series = q.all()

        # Bind variables to the view
        list_view = ListView(item_strings=[i.title for i in series])
        self.add_widget(list_view)
