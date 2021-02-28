from django.db import connection


class FetchCursor:
    cursor = None

    def __init__(self):
        self.cursor = connection.cursor()

    def execute(self, query):
        self.cursor.execute(query)
        return self

    def dictfetchall(self):
        "Returns all rows from a cursor as a dict"
        desc = self.cursor.description
        return [
            dict(zip([col[0] for col in desc], row))
            for row in self.cursor.fetchall()
        ]
