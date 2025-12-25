# 547. Number of Provinces

class Solution:
    def findCircleNum(self, nums: List[List[int]]) -> int:
        count = 0
        
        def dfs(nums, visited, i):
            for j in range(len(nums[0])):
                if nums[i][j] == 1 and not visited[j]:
                    visited[j] = 1
                    dfs(nums, visited, j)
            
        
        visited = [0]*len(nums)
        count = 0
        
        for i in range(len(nums)):
            if visited[i] == 0:
                dfs(nums, visited, i)
                count+=1
        return count
        