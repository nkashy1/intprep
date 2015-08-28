# Enter your code here. Read input from STDIN. Print output to STDOUT
square_matrix_dimension = int(raw_input())

def read_row(_):
    return map(int, raw_input().split())

rows = map(read_row, range(square_matrix_dimension))

def diagonal(i):
    return rows[i][i]

def antidiagonal(i):
    return rows[i][square_matrix_dimension - i - 1]

def run():
    return abs(sum(map(diagonal, range(square_matrix_dimension))) - sum(map(antidiagonal, range(square_matrix_dimension))))

print run()
