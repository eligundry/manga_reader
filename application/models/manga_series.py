from datetime import datetime

import requests
from sqlalchemy import Column, Text, String, Integer, SmallInteger, DateTime

from application.models import db, Base, IDMixin, CreatedModifiedMixin
from config import MANGAEDEN_API_URL

class MangaSeries(Base, IDMixin, CreatedModifiedMixin):
    __tablename__ = 'manga_series'

    manga_edan_id = Column(Integer, nullable=False, unique=True)
    title = Column(String(length=255), nullable=False)
    alias = Column(String(length=255), nullable=True)
    _status = Column('status', SmallInteger, nullable=False)
    image_path = Column(Text, nullable=True)
    last_chapter_date = Column(DateTime, nullable=True)

    @staticmethod
    def hydrate(lang='english'):
        """
        Updates the MangaList table by loading all the mangas from MangaEden

        @param lang: The language the list should be in ('english' or 'italian'
        @type lang: str
        """
        # MangaEden only has English and Italian and requires it as an int
        lang = int(lang == 'english')
        url = '{}/list/{}/'.format(MANGAEDEN_API_URL, lang)

        r = requests.get(url)

        for manga in r.json():
            series = MangaSeries()
            series.manga_edan_id = manga['i']
            series.title = manga['t']
            series.alias = manga['a']
            series._status = manga['s']
            series.image_path = manga['im']
            series.last_chapter_date = datetime.fromtimestamp(float(manga['ld']))

            db.add(series)

        db.commit()
