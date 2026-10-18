class Solution:
    """
    Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]

    New representation:
    [1,2,0,0,2,0,0,1,0,0,0]

    [3, 4.5, 10, 3]

    [(4,2), (1,2), (0,1), (7,1)] -> sort -> [(0,1), (1,2), (4,2), (7,1)]
    aux = [(4,3), (1,4.5), (0,10), (7,3)] -> sort -> [(0,10), (1,4.5), (4,3), (7,3)]

    s = [aux[-1]] = [(7,3), (1, 4.5), (0, 10)] len(s) -> 3

    input = [(0,10)] target 10
    aux = [(0, 1)]
    """

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        aux = []
        for i in range(len(position)):
            aux.append((
                position[i],
                (target - position[i]) / speed[i]
            ))
        aux.sort()  # O(N * log N)

        s = []
        s.append(aux[-1])

        for i in range(len(position) - 2, -1, -1):
            if aux[i][1] > s[-1][1]:
                s.append(aux[i])

        return len(s)
            
