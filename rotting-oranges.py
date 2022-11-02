#TC: O(m*n) 
#SC: O(m*n ) 

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int: 


        m = len(grid)  #describe m and n
        n = len(grid[0]) 
        time  = 0  #initially time is 0 
        freshcount = 0  #freshcounty is also initially zero
        q = deque() 
        directions = [[-1,0], [0,-1], [1,0], [0,1]] #initialize the directions array
        for i in range(m):  #traverse into the matrix
            for j in range(n):  
                if grid[i][j] == 2: #if the element is rotten, append it to q
                    q.append((i,j)) 
                elif grid[i][j] == 1:  #if it is fresh, append it to freshcount
                    freshcount+=1 

        while q and freshcount!=0: #go with q
            time+=1   #time will increase by one everytime
            size = len(q)  
            for _ in range(size): #traverse through the array

                curr = q.popleft()  #curr node is assigned to curr

                for r,c in directions:  #now check all the directions
                    nr = r + curr[0]  #neighbouring row is assigned
                    nc = c + curr[1]  #nc will be the neighbouring column

                    if nr>=0 and nr<m and nc>=0 and nc<n:  #check the boundary directions
                        if grid[nr][nc] == 1: #if the neighblour is fresh, then rot it
                            grid[nr][nc] = 2 
                            freshcount -= 1  #now decrease the freshcount
                            q.append((nr,nc)) 

        return time if freshcount == 0 else -1 #if there's no other fresh ones, return the time, else return -1
