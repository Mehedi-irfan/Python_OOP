class Messenger:
    def send_message(self, message=None, to=None, urgent=False):
        """
        send_message() → "No message"
        send_message("Hello") → "Message: Hello"
        send_message("Hi", "Alice") → "To Alice: Hi"
        send_message("Emergency", "Bob", True) → "🚨 URGENT To Bob: Emergency"
        """
        if message is None and to is None:
            return "No message"
        elif to is None and not urgent:
            return f"Message : {message}"
        elif urgent:
            return f"URGENT to {to} : {message}"
        else:
            return f"to {to} : {message}"


# Test cases:
msg = Messenger()
print(msg.send_message())  # "No message"
print(msg.send_message("Hello"))  # "Message: Hello"
print(msg.send_message("Hi", "Alice"))  # "To Alice: Hi"
print(msg.send_message("Emergency", "Bob", True))  # "🚨 URGENT To Bob: Emergency"
