class Solution:
    @staticmethod
    def isValid(s):
        Map = {")": "("}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack

    def generateParenthesis(self, n, s = ''):
        n *= 2
        combinations = []
        def recursive(n, s):
            if n == 0:
                if self.isValid(s):
                    combinations.append(s)
                return s
            
            recursive(n - 1, s + '(')
            recursive(n - 1, s + ')')
        recursive(n, s)
        return combinations
