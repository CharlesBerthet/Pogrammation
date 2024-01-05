from numpy import true_divide


A = [[1, 3, 5], [2, 4, 6], [7, 8, 0]]
A[2][1] = 18

for line in A:
    print(line)

def is_carree(A):
    if len(A)==len(A[0]):
        return 'True'
    else:
        return 'False'


B = [[0 for i in range(3)] for i in range(2)]

for line in B:
    print(line)




