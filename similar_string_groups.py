class Solution:  
    size = 0
    def numSimilarGroups(self, strs: List[str]) -> int:
            def find(x):
                if ds[x] != x:
                    ds[x] = find(ds[x]) #path compression
                return ds[x]
            
            
            def union(x, y):
                global size
                xfind = find(x)
                yfind = find(y)

                if xfind != yfind:
                    ds[yfind]=xfind
                    size-=1
                    
            def check(s1, s2):
                count=0
                for i in range(len(s1)):
                    if s1[i] != s2[i]:
                        count+=1
                        if count>2:
                            return False
                return True

            ds = [i for i in range(len(strs))]
            global size
            size = len(strs)
            
            for i in range(len(strs)):
                for j in range(i+1, len(strs)):
                    if check(strs[i],strs[j]):
                        union(i,j)
            # print(ds)
            return size