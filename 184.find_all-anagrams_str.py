class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        store = dict()
        for ele in p:
            if(ele in store):
                store[ele]+=1
            else:
                store[ele]=1
        
        i = 0
        j = 0
        store2 = dict()
        res = []
        while(j<len(s)):
            if(s[j] in store):
                if(s[j] in store2):
                    store2[s[j]]+=1
                else:
                    store2[s[j]]=1
                
            if(j-i+1<len(p)):
                j+=1
            else:
                if(store==store2):
                    res.append(i)
                if(s[i] in store2):
                    store2[s[i]]-=1
                    if(store2[s[i]]==0):
                        del store2[s[i]]
                i+=1
                j+=1
        
        return res
