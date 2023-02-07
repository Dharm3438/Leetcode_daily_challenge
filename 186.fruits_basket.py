class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i = 0
        j = 0
        maxi = 0
        store = dict()
        while(j<len(fruits)):
            if(fruits[j] in store):
                store[fruits[j]]+=1
            else:
                store[fruits[j]]=1
            
            if(len(store)<=2):
                maxi = max(maxi,j-i+1)
                j+=1
            else:
                while(len(store)>2):
                    store[fruits[i]]-=1
                    if(store[fruits[i]]==0):
                        del store[fruits[i]]
                    i+=1
                j+=1
        
        return maxi
