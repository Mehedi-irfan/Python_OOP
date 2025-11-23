import time


class MySQLConnection:
    def connect(self):
        time.sleep(0.5)
        return "Connect to MySQL Database"

    def execute(self, query):
        return f"Executing MySQL Query {query}"

    def disconnect(self):
        return "MySQL Connection Closed"

    def __str__(self):
        return "MySQL Connector"


class MongoDBConnection:
    def connect(self):
        time.sleep(0.3)
        return "Connect to MongoDB Database"

    def execute(self, query):
        return f"Executing MongoDB Query {query}"

    def disconnect(self):
        return "MongoDB Connection Closed"

    def __str__(self):
        return "MongoDB Connector"


class SQLiteConnection:
    def connect(self):
        time.sleep(0.1)
        return "Connect to SQLite Database"

    def execute(self, query):
        return f"Executing SQLite Query {query}"

    def disconnect(self):
        return "SQLite Connection Closed"

    def __str__(self):
        return "SQLite Connector"


class DatabaseManager:
    def __init__(self):
        self.connections = []

    def addConnection(self, connection):
        self.connections.append(connection)
        return f"Added {connection}"

    def execute_on_all(self, query):
        for connection in self.connections:
            print(f"{connection.connect()}")
            print(f"{connection.execute(query)}")
            print(f"{connection.disconnect()}")


db_manager = DatabaseManager()

mySql = MySQLConnection()
mongoDB = MongoDBConnection()
sqLite = SQLiteConnection()

db_manager.addConnection(mySql)
db_manager.addConnection(mongoDB)
db_manager.addConnection(sqLite)

db_manager.execute_on_all("SELECT * FROM users")
