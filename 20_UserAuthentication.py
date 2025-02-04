
from abc import ABC, abstractmethod

class UserAuthentication(ABC):

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

class GoogleAuth(UserAuthentication):

    def login(self):
        print("Logged into Google Sucesssfully!!")

    def logout(self):
        print("Logged out from Google Sucesssfully!!")

class FacebookAuth(UserAuthentication):

    def login(self):
        print("Logged into Facebook Sucesssfully!!")

    def logout(self):
        print("Logged out from Facebook Sucesssfully!!")

G=GoogleAuth()
G.login()
G.logout()

F=FacebookAuth()
F.login()
F.logout()