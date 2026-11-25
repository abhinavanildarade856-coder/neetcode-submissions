class Solution:
    def tribonacci(self, n: int) -> int:

        cache = {0:0 , 1:1 , 2:1 }

    
        def fn(x):
            
            if x in cache:
                return cache[x]

            if x not in cache:
                cache[x] = fn(x-1) + fn(x-2) + fn(x-3)

            return cache[x]


        return fn(n)