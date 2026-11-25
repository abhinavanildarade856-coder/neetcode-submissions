class Solution:
    def tribonacci(self, n: int) -> int:

        cache = {0:0 , 1:1 , 2:2 }

    
        def fn(x):
            if x == 0:
                return 0 

            if x == 1:
                return 1 
            
            if x == 2:
                return 1 

            if x in cache:
                return cache[x]

            if x not in cache:
                cache[x] = fn(x-1) + fn(x-2) + fn(x-3)

            return fn(x-1)  +  fn(x-2) + fn(x-3)


        return fn(n)