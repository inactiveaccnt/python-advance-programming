#date: 2018.08.18
#c * C

cons = 5;
c_matrix = [
            [2, 6, 7],
            [3, 25, 8],
            [9, 14, 15]
            ]
def solve(cons):
    for i in range(3):
        for j in range(3):
            c_matrix[i][j] *= cons
    return c_matrix

sol = solve(cons)

print(sol)
