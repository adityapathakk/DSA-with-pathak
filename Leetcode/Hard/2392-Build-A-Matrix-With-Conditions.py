class Solution: # revise this question, check approach below/solutions on leetcode for alternate methods/ideas
    def dfs(self, node: int, adj: defaultdict, visited: List[int], order: List[int], hasCycle: List[bool]):
        visited[node] = 1 # mark node as visiting
        
        for neighbor in adj[node]:
            if visited[neighbor] == 0:
                self.dfs(neighbor, adj, visited, order, hasCycle)
                if hasCycle[0]: # early exit if a cycle is detected
                    return
            elif visited[neighbor] == 1: # cycle detected
                hasCycle[0]  = True
                return
            
        visited[node] = 2 # mark node as visited
        order.append(node) # add node to the order

    def topologicalSort(self, edges: List[List[int]], n: int) -> List[int]:
        adj, order, visited, hasCycle = defaultdict(list), [], [0] * (n + 1), [False]

        for x, y in edges: # building adjacency list
            adj[x].append(y)
        
        for i in range(1, n + 1):
            if visited[i] == 0:
                self.dfs(i, adj, visited, order, hasCycle)
                if hasCycle[0]: # return empty if cycle detected
                    return []
        
        order.reverse() # reverse to get the correct order
        return order

    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        orderRows = self.topologicalSort(rowConditions, k) # store the topologically sorted sequences
        orderColumns = self.topologicalSort(colConditions, k)

        if not orderRows or not orderColumns: # if no topological sort exists, return empty array
            return []
        
        matrix = [[0] * k for _ in range(k)]
        posRow = {num: i for i, num in enumerate(orderRows)}
        posCol = {num: i for i, num in enumerate(orderColumns)}

        for num in range(1, k + 1):
            if num in posRow and num in posCol:
                matrix[posRow[num]][posCol[num]] = num
        
        return matrix


''' Leetcode Editorial Approach

During depth-first traversal in a graph, starting from node A, DFS explores all paths stemming from A before completing its recursion for A and moving to other nodes. Consequently, all nodes in these paths have A as an ancestor, making A a prerequisite for all paths originating from it.
Now, we know how to get all the integers that have a particular integer as a prerequisite. If a valid ordering of integers is possible, the node A would come before all the other sets of integers that have it as a prerequisite. This idea for solving the problem can be explored using a depth-first search.
Initialize a recursive function given by dfs where the recursive stack will contain the topologically sorted order of the courses in our graph. Construct the adjacency list from input edge pairs, where [a, b] denotes that course a must precede course b, forming edges a ➔ b in the graph.
For each node in our graph, we will run a depth-first search in case that node was not already visited in some other node's DFS traversal. Once the processing of all the neighbors is done, we will add this node to the stack. We are using the recursion stack to simulate the ordering we need.
Once all the nodes have been processed, we will return the nodes as they are returned in the recursion stack from top to bottom.
Now that we have topologically sorted arrays for both rowConditions and colConditions, how can we utilize them to construct the matrix? Each row and column should correspond to their respective sorted arrays. Therefore, the value at position matrix[i][j] is derived from rowConditions[i] and colConditions[j].

'''
