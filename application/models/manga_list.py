import requests

from application.models import IDMixin, CreatedModifiedMixin

class MangaList(IDMixin, CreatedModifiedMixin):

    def update(self):
        pass
