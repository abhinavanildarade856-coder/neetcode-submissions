class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res= []

        def bt(openn , closee):
            if openn == closee ==n:
                res.append("".join(stack))
                return

            if openn < n:
                stack.append("(")
                bt(openn+1 ,closee)
                stack.pop()


            if closee < openn:
                stack.append(")")
                bt(openn ,closee+1)
                stack.pop()
        bt(0,0)
        return res