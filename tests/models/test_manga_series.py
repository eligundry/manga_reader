from application.models import db, MangaSeries
from tests import BaseTestCase

class TestMangaSeriesHydrate(BaseTestCase):

    def test_hydrate(self):
        # Load up 25 series in the db
        MangaSeries.hydrate(page=1, per_page=25)

        # Query them all
        series = db.query(MangaSeries).all()
        assert len(series) == 25
