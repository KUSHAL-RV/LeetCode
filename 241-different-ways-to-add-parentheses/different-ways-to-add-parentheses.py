class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        res=[]
        if expression.isdigit():
            return [int(expression)]
        for i , ch in enumerate(expression):
            if ch in '+-*':
                left=self.diffWaysToCompute(expression[:i])
                right=self.diffWaysToCompute(expression[i+1:])
            
                for a in left:
                    for b in right:
                        if ch=='+':
                            res.append(a+b)
                        elif ch=='-':
                            res.append(a-b)
                        else:
                            res.append(a*b)
        return res
        