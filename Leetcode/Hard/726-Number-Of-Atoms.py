class Solution: # editorial solution - stack | should be revised for better understanding
    def countOfAtoms(self, formula: str) -> str:
        stack = [defaultdict(int)] # stack to keep track of the atoms and their counts
        index = 0 # index to keep track of the current character

        while index < len(formula): # parsing the formula
            # if '(', insert new hashmap to the stack; keep track of atoms and their counts in the nested formula
            if formula[index] == "(":
                stack.append(defaultdict(int))
                index += 1

            # if ')', pop top element from the stack; multiply count with multiplicity of the nested formula
            elif formula[index] == ")":
                curr_map = stack.pop()
                index += 1
                multiplier = ""
                while index < len(formula) and formula[index].isdigit():
                    multiplier += formula[index]
                    index += 1
                if multiplier:
                    multiplier = int(multiplier)
                    for atom in curr_map:
                        curr_map[atom] *= multiplier

                for atom in curr_map:
                    stack[-1][atom] += curr_map[atom]

            # otherwise, it must be UPPERCASE LETTER. extract complete atom with frequency, and update most recent hashmap
            else:
                curr_atom = formula[index]
                index += 1
                while index < len(formula) and formula[index].islower():
                    curr_atom += formula[index]
                    index += 1

                curr_count = ""
                while index < len(formula) and formula[index].isdigit():
                    curr_count += formula[index]
                    index += 1

                if curr_count == "":
                    stack[-1][curr_atom] += 1
                else:
                    stack[-1][curr_atom] += int(curr_count)

        final_map = dict(sorted(stack[0].items())) # sorting final map

        ans = "" # generating answer string
        for atom in final_map:
            ans += atom
            if final_map[atom] > 1:
                ans += str(final_map[atom])

        return ans

''' Approach

Revise this question. Leetcode editorial for reference.

'''
