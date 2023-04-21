def read_matrix():
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        for e in x:
            r.append(float(e))
        m.append(r)
    return m


def mult_c(c, A):
    return [[c * a for a in row] for row in A]


def mult(A, B):
    if len(A[0]) != len(B):
        mult(B, A)
    C = [[sum(A[i][k] * B[k][j] for k in range(len(B)))
          for j in range(len(B[0]))] for i in range(len(A))]
    return C


exec(input().strip())  # ตอ้ งมคี ําส่ังนี้ ตรงน้ี ตอนสง่ ให้Grader ตรวจ
