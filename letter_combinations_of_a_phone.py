def letterCombinations(digits):
    letters = {"2": "abc",
               "3": "def",
               "4": "ghi",
               "5": "jkl",
               "6": "mno",
               "7": "pqrs",
               "8": "tuv",
               "9": "wxyz"
               }

    if len(digits) == 0:
        return []

    combinations = []

    def backtrack(idx, path):
        if len(path) == len(digits):
            combinations.append("".join(path))
            return

        chars = letters[digits[idx]]

        for c in chars:
            path.append(c)
            backtrack(idx + 1, path)
            path.pop()

    backtrack(0, [])
    return combinations


print(letterCombinations("234"))