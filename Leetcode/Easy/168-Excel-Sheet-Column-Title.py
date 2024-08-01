class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber:
            res = chr(ord('A') + (columnNumber - 1) % 26) + res
            columnNumber = (columnNumber - 1) // 26
        return res