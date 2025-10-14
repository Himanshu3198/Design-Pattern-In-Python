class Messages:
    def __init__(self, message: str, timestamp: int):
        self.message = message
        self.timestamp = timestamp


class Logger:

    def __init__(self):
        self.WINDOW_SIZE = 10
        self.track_message: Dict[str, int] = {}
        self.queue: List[Messages] = []

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:

        while len(self.queue) > 0 and (timestamp - self.queue[0].timestamp) >= self.WINDOW_SIZE:
            older_message = self.queue.pop(0)
            del self.track_message[older_message.message]

        if message not in self.track_message:
            self.track_message[message] = timestamp
            self.queue.append(Messages(message, timestamp))
            return True
        return False

    # Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)