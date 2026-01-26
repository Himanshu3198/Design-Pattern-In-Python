import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        INF = float('inf')
        n,m =  len(heights),len(heights[0])
        pq = [(0,0,0)]
        dist = [[INF]*m for _ in range(n)]
        dist[0][0] = 0
        direction = [(0,1),(1,0),(0,-1),(-1,0)]

        while len(pq)>0:
             effort,x,y = heapq.heappop(pq)
             if x == n-1 and y == m-1 : 
                return effort
             for dx,dy in direction:
                new_x,new_y = x+dx,y+dy
                if new_x <0 or new_y < 0 or new_x >=n or new_y >= m:
                   continue
                new_effort = max(effort,abs(heights[new_x][new_y]-heights[x][y]))
                if new_effort < dist[new_x][new_y]:
                    dist[new_x][new_y] = new_effort
                    heapq.heappush(pq,(new_effort,new_x,new_y))
        return 0


        
