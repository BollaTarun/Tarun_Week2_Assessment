
from abc import ABC,abstractmethod

class IDatabaseOperations(ABC):

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass

class SQLDatabase(IDatabaseOperations):

    def insert(self):
        print("SQL Database Insert!!")

    def update(self):
        print("SQL Database Update!!")

    def delete(self):
        print("SQL Database Delete!!")

class NoSQLDatabase(IDatabaseOperations):

    def insert(self):
        print("NoSQL Database Insert!!")

    def update(self):
        print("NoSQL Database Update!!")

    def delete(self):
        print("NoSQL Database Delete!!")

S=SQLDatabase()
S.insert()
S.update()
S.delete()

N=NoSQLDatabase()
N.insert()
N.update()
N.delete()