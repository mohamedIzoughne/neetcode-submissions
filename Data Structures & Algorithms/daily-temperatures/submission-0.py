class Solution:
    def dailyTemperatures(self, temps):
        result = [0] * len(temps)
        stack = deque()


        for i, v in enumerate(temps):
            if len(stack) == 0 or v <= stack[-1][1]:
                stack.append((i, v))
            else:
                while len(stack) != 0 and v > stack[-1][1]:
                    popped = stack.pop()
                    result[popped[0]] = i - popped[0]
                stack.append((i, v))
        return result