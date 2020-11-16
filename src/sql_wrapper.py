import sqlite3


class SQL:
    '''Provides a easy-to-use library for dealing Sqlite3 within the project'''

    def __init__(self, filename) -> None:
        _conn = sqlite3.connect(filename)
        self._c = _conn.cursor()

    def add(self, id, status=0):
        """
        Add a post to the database
        """
