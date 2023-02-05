class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        j = 0
        k = len(s1)
        store = dict()
        for val in s1:
            if(val in store):
                store[val]+=1
            else:
                store[val]=1
            
        store2 = dict()

        ct = 0
        while(j<len(s2)):
            if s2[j] in store:
                if(s2[j] in store2):
                    store2[s2[j]]+=1
                else:
                    store2[s2[j]]=1

            if(j-i+1<k):
                j+=1
            elif(j-i+1==k):
                if(store==store2):
                    return True
                if(s2[i] in store2):
                    store2[s2[i]]-=1
                    if(store2[s2[i]]==0):
                        del store2[s2[i]]
                i+=1
                j+=1
        
        return False
