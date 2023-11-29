import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.
    """
    a = np.array(m_a)
    b = np.array(m_b)
    if a.shape[1] != b.shape[0]:
        print("Error: The matrices cannot be multiplied.")
        return None
    c = np.dot(a, b)

    return c
