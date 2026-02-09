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


# 2d array memoization
class Solution:
    def solve(self,costs,dp,idx,prev)->int:
         if idx == len(costs):
            return 0
         if (idx,prev) in dp:
             return dp[(idx,prev)]
        
         res = float('inf')
         for color in range(0,3):
            if color == prev :
                continue

            ans = costs[idx][color]+self.solve(costs,dp,idx+1,color)
            res = min(res,ans)
         dp[(idx,prev)] = res
         return res
    def minCost(self, costs: List[List[int]]) -> int:

        dp = {}

        return min(costs[0][0]+self.solve(costs,dp,1,0),costs[0][1]+self.solve(costs,dp,1,1),costs[0][2]+self.solve(costs,dp,1,2))



# queue + sliding window
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:

        n = len(s)
        if s[n-1]  == '1' or s[0] == '1':
            return False

        q = []
        q.append(0)
        so_far = 0
        
        while q:

                curr = q.pop(0)
                if curr >= n-1:
                    return True
                start = max(curr+minJump,so_far+1)
                end = min(curr+maxJump,n-1)
                for j in range(start,end+1):
                    if j <= n-1 and s[j] == '0':
                       q.append(j)       
                so_far = end
            
        return False



class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encode = []
        for s in strs:
             encode.append(f"{len(s)}#{s}")
        
        return ''.join(encode)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        ans = []
        curr = ""
        i = 0
        while i < len(s):

            j = i
            while s[j] != '#':
               j  += 1
            
            sz = int(s[i:j])
            ans.append(s[j+1:j+1+sz])
            i = j+1+sz

        return ans
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))



from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        dq = deque()
        left = 0
        res = []

        for right in range(0,len(nums)):

            while dq and dq[-1] < nums[right]:
                  dq.pop()
            
            dq.append(nums[right])
            window = right-left+1

            if window == k:
                res.append(dq[0])
                if dq and dq[0] == nums[left]:
                    dq.popleft()
                left +=1
        
        return res


import heapq


class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        max_heap = []
        res = []

        for i,(x,y) in enumerate(points):
            dist = x*x+y*y
            heapq.heappush(max_heap,(-dist,i))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        while len(max_heap) > 0:
            _,idx =  heapq.heappop(max_heap)
            res.append(points[idx])
        return res
        
                

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
           return []

        # Mapping of digits to letters
        key_map = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        ans = []
        res = []
        def solve(res:List[str],idx:int)->None:
            if idx == len(digits):
                ans.append(''.join(res))
                return
            s = key_map.get(digits[idx],"")
            for c in s:
                res.append(c)
                solve(res,idx+1)
                res.pop()
        solve(res,0)
        return ans

        
        
        

