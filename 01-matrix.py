#TC: O(m*n) 
#SC: O(m*n)

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]: 


        m = len(mat) #assign the column of the matrix
        n= len(mat[0]) #assign the row of the matrix
        directions = [[0,1],[1,0],[0,-1],[-1,0]] #assign the directions array
        q = deque() #q will be the our queue
 
        for i in range(m): #traverse through the matrix
            for j in range(n): 
                if mat[i][j] == 0: #if the element is 0, append the index into q
                    q.append((i,j)) 
                else: 
                    mat[i][j] = -1 #else set the element to -1 

        dist = 0 
        while q:  #traverse through the queue
            size = len(q) 
            dist+=1 #everytime increase the distance by one while traversing through the q
            for _ in range(size): #traverse through the current level
                curr = q.popleft() 
                for x,y in directions: #find the neighbouring elements
                    nr = x+curr[0] 
                    nc = y+curr[1] 

                    if nr>=0 and nr<m and nc>=0 and nc<n and mat[nr][nc] == -1: #now, assign the distance only of element is -1
                        mat[nr][nc] = dist 
                        q.append((nr,nc)) #append the index to q

        return mat #return matrix