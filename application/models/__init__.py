class IDMixin(object):
    pass

class CreatedModifiedMixin(object):
    pass

from application.models.manga_list import MangaList

__all__ = [
    'IDMixin',
    'CreatedModifiedMixin',
    'MangaList',
]
