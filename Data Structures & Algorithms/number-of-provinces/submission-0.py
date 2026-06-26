class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        n = len(isConnected)
        visited = [False] * n

        def exploreAndMark(city):
            visited[city] = True
            for j in range(0, n):
                if isConnected[city][j] == 1 and not visited[j]:
                    exploreAndMark(j)

        for i in range(0, n):
            if not visited[i]:
                exploreAndMark(i)
                provinces += 1
            
        return provinces

