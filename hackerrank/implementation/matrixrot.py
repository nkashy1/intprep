def run(m, n, r, A):
    num_shells = min(m, n)/2

    def shell_length(k):
        return 2*(n - 2*k - 1) + 2*(m - 2*k - 1)

    def shell_index_to_matrix_index(k, l):
        horizontal_strip = n - 2*k - 1
        vertical_strip = m - 2*k - 1
        if 0 <= l < horizontal_strip:
            return (k, k+l)
        elif horizontal_strip <= l < horizontal_strip + vertical_strip:
            return (k + (l - horizontal_strip), n - 1 -k)
        elif horizontal_strip + vertical_strip <= l < 2*horizontal_strip + vertical_strip:
            return (m - 1 - k, n - 1 - k - (l - (horizontal_strip + vertical_strip)))
        elif 2*horizontal_strip + vertical_strip <= l < 2*horizontal_strip + 2*vertical_strip:
            return (m - 1 - k - (l - (2*horizontal_strip + vertical_strip)), k)

        raise ValueError("Invalid shell-index combination.")

    s2m = {}
    for k in range(num_shells):
        length = shell_length(k)
        for l in range(length):
            s2m[(k, l)] = shell_index_to_matrix_index(k, l)

    m2s = {v:k for (k,v) in s2m.items()}

    def post_rotation_value(i,j):
        (shell, shell_index) = m2s[(i, j)]
        matrix_index = s2m[(shell, (shell_index+r)%shell_length(shell))]
        return A[matrix_index[0]][matrix_index[1]]

    for i in range(m):
        row = []
        for j in range(n):
            row.append(str(post_rotation_value(i, j)))

        print " ".join(row)

params = map(int, raw_input().split())
m = params[0]
n = params[1]
r = params[2]

A = []
for _ in range(m):
    A.append(map(int, raw_input().split()))

run(m, n, r, A)