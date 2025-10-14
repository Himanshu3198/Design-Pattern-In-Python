def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """

    col: Set[int] = set()
    row: Set[int] = set()

    for i in range(0, len(matrix)):

        for j in range(0, len(matrix[i])):
            if matrix[i][j] == 0:
                row.add(i)
                col.add(j)

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if i in row or j in col:
                matrix[i][j] = 0

def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        col: set[int] = set()
        row: set[int] = set()

        for i in range(0, len(matrix)):

            for j in range(0, len(matrix[i])):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if i in row or j in col:
                    matrix[i][j] = 0


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


