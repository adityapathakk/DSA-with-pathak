# Link to problem: https://www.geeksforgeeks.org/problems/evaluation-of-postfix-expression1735/1

class Solution:
    def evaluatePostfix(self, S):
        stac = []
        ops = ["+", "-", "*", "/"]
        
        for i in S:
            if i in ops:
                a = int(stac.pop())
                b = int(stac.pop())
                
                if i == "+" : stac.append(b + a)
                elif i == "-" : stac.append(b - a)
                elif i == "*" : stac.append(b * a)
                elif i == "/" : stac.append(b / a)
            
            else:
                stac.append(i)

        return stac[-1]