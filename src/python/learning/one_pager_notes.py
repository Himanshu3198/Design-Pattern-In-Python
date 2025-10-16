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


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stk = []

        for asteroid in asteroids:
            alive = True
            while len(stk) > 0 and alive and stk[-1] > 0 and asteroid < 0:

                last_asteroid = stk[-1]
                current_asteroid = abs(asteroid)

                if last_asteroid == current_asteroid:
                    stk.pop()
                    alive = False
                elif last_asteroid > current_asteroid:
                    alive = False
                else:
                    stk.pop()

            if alive:
                stk.append(asteroid)

        ans = []

        while len(stk) > 0:
            ans.append(stk.pop())

        ans.reverse()

        return ans


import heapq


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        max_heap = []

        for sorted_list in lists:
            temp = sorted_list
            while temp:
                heapq.heappush(max_heap, temp.val)
                temp = temp.next

        result = ListNode(-1)
        new_head = result

        while len(max_heap) > 0:
            element = heapq.heappop(max_heap)
            result.next = ListNode(element)
            result = result.next

        return new_head.next



class Solution:
    def frequencySort(self, s: str) -> str:

        max_heap = []
        freq: Dict[char, int] = {}
        for t in s:
            freq[t] = freq.get(t, 0) + 1

        for c, count in freq.items():
            heapq.heappush(max_heap, (-count, c))

        ans = []

        while len(max_heap) > 0:
            count, c = heapq.heappop(max_heap)
            ans.append(c * -count)

        return "".join(ans)




