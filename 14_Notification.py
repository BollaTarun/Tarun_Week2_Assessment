
class Notification:

    def send(self):
        print("Notification is sent!!!\n")

class EmailNotification(Notification):

    def send(self):
        print("New Email has been sent.\n")

class SMSNotification(Notification):

    def send(self):
        print("New SMS has been sent.\n")

print("SMS :")
S=SMSNotification()
S.send()
print("Email :")
E=EmailNotification()
E.send()
print("Notification :")
N=Notification()
N.send()
