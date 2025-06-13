from typing import List

from moonreader_tools.datamodel.annotation import Note
from moonreader_tools.datamodel.statistics import Statistics


class Book:
    """
    Simple objects representing a MoonReader app book,
    with its statistics and attached notes if any
    """

    def __init__(self, title, stats=None, notes: List[Note] = None, last_modified = None) -> None:
        """
        :param title: Book title
        :param stats: Statistics object
        :param notes: list of Note objects
        """
        self.title = title
        self.stats = stats
        self.stats = stats or Statistics.empty_stats()
        self.notes = notes or []
        self.last_modified = last_modified

    @property
    def pages(self):
        return self.stats.pages

    @pages.setter
    def pages(self, value):
        self.stats.pages = value

    @property
    def stats(self):
        return self.__stats

    @stats.setter
    def stats(self, stats_obj):
        self.__stats = stats_obj

    @property
    def percentage(self):
        return self.stats.percentage

    @percentage.setter
    def percentage(self, value):
        self.stats.percentage = value

    def to_dict(self):
        """Serialize book to dictionary"""
        book_dict = {
            "title": self.title,
            "pages": self.pages,
            "percentage": self.percentage,
            "last_modified": self.last_modified,
            "notes": [note.to_dict() for note in self.notes],
        }
        return book_dict

    def __str__(self):
        return "<Book> {}: {} notes".format(self.title, len(self.notes))

    def __repr__(self):
        return str(self)
