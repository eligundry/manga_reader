from datetime import datetime

import requests
from sqlalchemy import Column, Text, String, Integer, SmallInteger, DateTime

from application.models import db, Base, IDMixin, CreatedModifiedMixin
from config import MANGAEDEN_API_URL

class MangaSeries(Base, IDMixin, CreatedModifiedMixin):
    __tablename__ = 'manga_series'

    manga_edan_id = Column(String(255), nullable=False, unique=True)
    title = Column(String(length=255), nullable=False)
    alias = Column(String(length=255), nullable=True)
    _status = Column('status', SmallInteger, nullable=False)
    image_path = Column(Text, nullable=True)
    last_chapter_date = Column(DateTime, nullable=True)
    last_visited = Column(DateTime, nullable=True)

    @staticmethod
    def hydrate(page=None, per_page=None, lang='english'):
        """
        Updates the MangaList table by loading all the mangas from MangaEden

        @param page: The page to begin with in the results
        @type page: int|None
        @param per_page: The amount of results to return per page
        @type per_page: int|None
        @param lang: The language the list should be in ('english' or 'italian')
        @type lang: str
        """
        params = {}
        if per_page and not page:
            raise ArgumentError('MangaSeries.hydrate requires that either just'
                                ' page or page and per_page are specified.')

        # Setup pagination, if needed
        if page:
            params['p'] = per_page

        if per_page:
            params['l'] = per_page

        # MangaEden only has English and Italian and requires it as an int
        lang = int(lang == 'english')
        url = '{}/list/{}/'.format(MANGAEDEN_API_URL, lang)


        # Make the request
        r = requests.get(url, params=params)

        if 'manga' not in r.json():
            # @TODO Surface an exception
            return

        for manga in r.json()['manga']:
            try:
                lts = datetime.fromtimestamp(float(manga.get('ld')))
            except TypeError:
                lts = None

            series = MangaSeries()
            series.manga_edan_id = manga['i']
            series.title = manga['t']
            series._status = manga['s']
            series.alias = manga.get('a')
            series.image_path = manga.get('im')
            series.last_chapter_date = lts

            db.add(series)

        db.commit()
