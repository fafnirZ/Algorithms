'''
Implements power using memoization
using dictionary, OPT array and divide and conquer
O(log(n)) time complexity

'''
class Solution:
    def __init__(self):
        self.opt= dict({})
        
        
    def memo(self, x: float, n:int):
        if(n in self.opt):
            # O(1) lookup
            return (self.opt[n])
        else:
            if(n == 0):
                self.opt[n] = 1
            elif(n == 1):
                self.opt[int(n)] = float(x)
            elif(n == -1):
                self.opt[int(n)] = float(x**-1)
            elif(n % 2 == 0):
                self.opt[int(n)] = float(self.memo(x, n/2)) * float(self.memo(x,n/2))
            else:
                self.opt[int(n)] = float(self.memo(x, (n-1)/2)) * float(self.memo(x,(n-1)/2)) * x
              
            return self.opt[n]
                
                
    def myPow(self, x: float, n: int) -> float:
        opt = dict({})
        return self.memo(x,n)