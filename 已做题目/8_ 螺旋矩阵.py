class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        def veer(dx,dy):
            if (dx,dy) == (0,1):
                dx,dy = 1,0
            elif (dx,dy) == (1,0):
                dx,dy = 0,-1
            elif (dx,dy) == (0,-1):
                dx,dy = -1,0
            else:
                dx,dy = 0,1
            return (dx,dy)
        m = len(matrix)
        n = len(matrix[0])
        t,dx,dy,x,y,num_list = 0,0,1,0,0,[]
        while t < n*m:
            num_list.append(matrix[x][y])
            t += 1
            matrix[x][y] = float('inf')
            if x+dx in range(m) and y+dy in range(n) and matrix[x+dx][y+dy] != float('inf'):
                x,y = x+dx,y+dy
            else:
                dx,dy = veer(dx,dy)
                x,y = x+dx,y+dy
        return num_list