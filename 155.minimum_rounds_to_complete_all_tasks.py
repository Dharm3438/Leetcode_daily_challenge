class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        store = dict()
        for val in tasks:
            if val in store:
                store[val]+=1
            else:
                store[val]=1
        
        ct=0
        print(store)
        for key,val in store.items():
            # if(val%3!=1):
                # ct+=math.ceil(val/3)
            # elif(val%2!=1):
                # ct+=math.ceil(val/2)
            if(val==1):
                return -1
            elif(val==2):
                ct+=1
            elif(val==3):
                ct+=1
            else:
                while(val>4):
                    val-=3
                    ct+=1
                if(val%2==0):
                    ct+=val//2
                elif(val%3==0):
                    ct+=val//3
                else:
                    return -1
        return int(ct)
