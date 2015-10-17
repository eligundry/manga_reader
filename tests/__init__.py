import unittest
from abc import ABCMeta

from application.models import setup_database, Base

class BaseTestCase(unittest.TestCase):
    __metaclass__ = ABCMeta

    def setUp(self):
        # Create the database in memory
        self.engine, self.db = setup_database(db_location='sqlite://')
        Base.metadata.create_all(self.engine)

    def tearDown(self):
        Base.metadata.drop_all(self.engine)
