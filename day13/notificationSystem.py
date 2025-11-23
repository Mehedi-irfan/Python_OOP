class EmailSender:
    def send(self, message, recipient):
        return f"E-mail send to {recipient} : {message}"

    def getStatus(self):
        return "E-mail service Active"


class SMSSender:
    def send(self, message, recipient):
        return f"SMS Sender {recipient} : {message}"

    def getStatus(self):
        return "SMS Service : Ready"


class PushNotification:
    def send(self, message, recipient):
        return f"Push Notification {recipient} :{message}"

    def getStatus(self):
        return "Push Service : Connected"


class NotificationManager:
    def __init__(self):
        self.senders = []

    def addSenders(self, sender):
        self.senders.append(sender)
        print(f"added {sender.getStatus()}")

    def boardCast(self, message, recipients):
        for sender in self.senders:
            for recipient in recipients:
                print(sender.send(message, recipient))


manager = NotificationManager()

email = EmailSender()
sms = SMSSender()
push = PushNotification()

manager.addSenders(email)
manager.addSenders(sms)
manager.addSenders(push)

recipients = ["alice@email.com", "+8801712345678", "user123"]
manager.boardCast("Hello! This is a test message", recipients)
