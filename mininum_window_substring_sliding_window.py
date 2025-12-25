class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i,j = 0, 0
        
        mp = {}
        
        for c in t:
            mp[c] = 1+mp.get(c,0)
        
        count = len(mp)
        
        exists = 0
        res_length = float('inf')
        sidx,eidx = -1,-1
        
        for j in range(len(s)):
            if exists < count:
                if s[j] in mp:
                    mp[s[j]]-=1
                    if mp[s[j]] == 0:
                        exists+=1
            
            if exists == count:
                while exists == count:
                    if j-i+1 < res_length:
                        sidx, eidx = i,j
                        res_length = j-i+1

                    rm = s[i]
                    if rm in mp:
                        if mp[rm] == 0:
                            mp[rm]+=1
                            exists-=1
                        else:
                            mp[rm]+=1
                    i+=1

        return s[sidx:eidx+1]
                    
                    