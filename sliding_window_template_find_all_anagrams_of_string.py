class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        i,j = 0,0
        p_mp = {}
        
        for item in p:
            p_mp[item] = 1+p_mp.get(item,0)
            
        st = deque(p)
        res = []
        tmp_mp = {}
        tmp = deque()
        while j < len(s):
            if len(tmp) < len(p):
                tmp.append(s[j])
                tmp_mp[s[j]]=1+tmp_mp.get(s[j],0)
                
            if len(tmp) == len(p):
                if tmp_mp == p_mp:
                    res.append(i)
                rm = tmp.popleft()
                if tmp_mp[rm] == 1:
                    del tmp_mp[rm]
                else:
                    tmp_mp[rm]-=1
                i+=1
            j+=1
        return res
