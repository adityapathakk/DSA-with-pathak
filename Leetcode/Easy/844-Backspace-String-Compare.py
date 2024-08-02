class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackS, stackT = [], []

        for i in s:
            if i == "#":
                if len(stackS) > 0:
                    stackS.pop()
            else:
                stackS.append(i)
        
        for j in t:
            if j == "#":
                if len(stackT) > 0:
                    stackT.pop()
            else:
                stackT.append(j)

        return stackS == stackT