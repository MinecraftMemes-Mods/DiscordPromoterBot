import sqlite3


class SQL:
    '''Provides an easy-to-use library for dealing with the database within the project'''

    def __init__(self, filename) -> None:
        self._conn = sqlite3.connect(filename)
        self._c = self._conn.cursor()

    def add(self, id) -> bool:
        """
        Add a post to the database.
        """

        params = (id,)
        self._c.execute(
            'INSERT INTO posts VALUES (?, strftime("%s", "now"));', params)
        self._conn.commit()

    def get(self, id) -> bool:
        """
        Fetches the status of a post
        """

        params = (id,)
        self._c.execute('SELECT 0 FROM posts WHERE id=?;', params)

        # result of fetchone should be either (0,) or None
        return bool(self._c.fetchone())
