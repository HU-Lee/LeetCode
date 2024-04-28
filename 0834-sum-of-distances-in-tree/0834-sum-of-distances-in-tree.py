class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)

        subnodes = [0]*n
        sums = [0]*n
        def dfs_subnode(i: int, parent:int):
            for x in graph[i]:
                if x != parent:
                    dfs_subnode(x,i)
                    subnodes[i] += subnodes[x]+1
                    
                    # Add sum, with previous child value + 1*subnodes
                    sums[i] += sums[x] + (subnodes[x]+1)
        
        dfs_subnode(0,-1)

        # now subnodes stores count, sums have depth sum from the root
        print(subnodes)
        print(sums)
        # only sums[0] is valid, so another process

        def dfs_count(i: int, parent: int):
            for x in graph[i]:
                if x != parent:
                    # subnodes are more close to x, and others are not
                    # x~i distances are constant, so exclude these two
                    sums[x] = sums[i] - subnodes[x] + (n-2-subnodes[x])
                    dfs_count(x,i)
        
        dfs_count(0,-1)

        return sums