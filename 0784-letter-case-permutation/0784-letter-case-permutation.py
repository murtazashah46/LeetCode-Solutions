class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        answer = []
        answer.append("")
        for char in s:
            n = len(answer)
            if(char in "0123456789"):
                for i in range(n):
                    answer[i] += char
            else:
                for i in range(n):
                    string = answer[i]
                    string += char.upper()
                    answer[i] += char.lower()
                    answer.append(string)
        return answer