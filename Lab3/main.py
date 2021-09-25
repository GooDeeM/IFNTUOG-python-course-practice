import random

def pretty_print_matrix(matrix: list):
    for m in matrix:
        print('\t'.join(map(str, m)))

if __name__ == '__main__':
    print('Task 1:')
    n = 10
    # n = int(input())
    A = [random.randint(0, 50) for _ in range(n)]
    X = A[::2]
    Y = A[1::2]
    print(f'A = {A}\nX = {X}\nY = {Y}')

    print('Task 2:')
    n, m = len('Dmytro'), len('Popoilyk')
    A = [[random.randint(-10, 10) for _ in range(n)] for _ in range(m)]
    
    print('Given matrix:')
    pretty_print_matrix(A)

    print('Updated matrix')
    for index, m in enumerate(A):
        A[index] = [0 for _ in range(index if index < len(m) else len(m))] + m[index:]
    pretty_print_matrix(A)

