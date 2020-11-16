import sqlite3


class SQL:
    '''Provides a easy-to-use library for dealing Sqlite3 within the project'''

    def __init__(self, filename) -> None:
        _conn = sqlite3.connect(filename)
        self._c = _conn.cursor()

    def add(self, id, status=0) -> None:
        """
        Add a post to the database.
        `status==0` if the post does not have a comment yet, `status==1` if the comment has already been made.
        """

        params = (id, status)
        self._c.execute('INSERT INTO posts VALUES (?, ?);', params)

    def get(self, id) -> bool:
        """
        Fetches the status of a post
        """

        params = (id,)
        self._c.execute('SELECT status FROM posts WHERE id=?;', params)

        # since we're dealing with either 0 or 1, we can simply use them as a bool
        return self._c.fetchone()[0]

    def set(self, id, status) -> None:
        """
        Sets the status of a post
        """

        params = (id, status)

        self._c.execute('UPDATE posts SET status=? WHERE id=?;', params)
