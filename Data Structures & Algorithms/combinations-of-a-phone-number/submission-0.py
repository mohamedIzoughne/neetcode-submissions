class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_chars = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        if len(digits) == 0:
            return []

        result = []

        def combinations(index=0, word = ""):

            if index == len(digits):
                result.append(word)
                return
            

            letter = digits[index]
            for i in digit_chars[letter]:
                combinations(index + 1, f"{word}{i}")

        combinations()
        return result

