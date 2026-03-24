# NAGA-RESEARCH | Matrix Library
# Day 1 - Foundation 

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]


    def __repr__(self):
        return '\n'.join([str(row) for row in self.data])
    

# Test
m = Matrix(3,3)
print(m)