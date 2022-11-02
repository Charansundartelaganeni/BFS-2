#TC: O(n) 
#SC: O(h)
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int: 

        self.d = {}
        for i in employees: #save the importance and subordinates as value for the key id in hashmap
            self.d[i.id] = i 
        return self.dfs(id) 

    def dfs(self,  id):
        employee = self.d[id] #current employee is assigned by getting searched in hashmap with id as key
        importance = 0 #set the importance as zero
        for i in employee.subordinates: #traverse through all the subordinates
            importance += self.dfs(i) #while traversing add all the importances of subordinates
        return employee.importance + importance