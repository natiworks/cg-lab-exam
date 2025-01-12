

import numpy as np

def reconstruct_matrix(U, S, VT):
    return U @ np.diag(S) @ VT


A = np.array([
    [3, 4, 3],
    [1, 2, 3],
    [4, 2, 1]
])


U, D, VT = np.linalg.svd(A)


print(U)
print(D)
print(VT)


A_remake = reconstruct_matrix(U, D, VT)
print("Reconstructed Matrix:\n", A_remake)
