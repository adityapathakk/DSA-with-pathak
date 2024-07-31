class Solution: # vertical scanning - compare characters from top to bottom on the same column/same character index of strings before moving on to the next column
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = len(strs)
        if strs is None or length == 0:
            return "" # no common prefix
        
        firstWord = strs[0]
        for i in range(len(firstWord)):
            char = firstWord[i] 
            for j in range(1, length):
                if i == len(strs[j]) or strs[j][i] != char: # comparing the same character of all strings
                    return firstWord[:i]

        return firstWord