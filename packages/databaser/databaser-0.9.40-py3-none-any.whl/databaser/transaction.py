from databaser.engine.engine import DatabaseEngine


class Transaction:
    def __init__(self, conn_string):
        self.__sql = []
        self.conn_string = conn_string

    def add(self, sql: str):
        self.__sql.append(sql)
        return self

    def get_sql(self):
        return "".join(self.__sql)

    def commit(self):
        return DatabaseEngine(**self.conn_string).execute(
            self.get_sql(),
            transaction=True
        )

    def show(self):
        return DatabaseEngine(**self.conn_string).execute(
            self.get_sql(),
            transaction=True,
            has_return=True,
            return_many=True
        )

    def show_one(self):
        return DatabaseEngine(**self.conn_string).execute(
            self.get_sql(),
            transaction=True,
            has_return=True,
            return_many=False
        )
