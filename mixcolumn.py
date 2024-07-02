#from copy import copy


def multiply(a, b):
    """
    Operasi perkalian dalam Galois Field (GF(2^8)).
    """
    p = 0
    while a and b:
        if b & 1:
            p ^= a
        a <<= 1
        if a & 0x100:
            a ^= 0x11b  # x^8 + x^4 + x^3 + x + 1
        b >>= 1
    return p & 0xff



def mixcol(state):
    
    r = [[2,3,1,1],[1,2,3,1],[1,1,2,3],[3,1,1,2]]
    
    for i in range(4):
        temp = [state[j][i] for j in range(4)]
        state[0][i] = multiply(temp[0], r[0][0]) ^ multiply(temp[1], r[0][1]) ^ multiply(temp[2], r[0][2]) ^ multiply(temp[3], r[0][3])
        state[1][i] = multiply(temp[0], r[1][0]) ^ multiply(temp[1], r[1][1]) ^ multiply(temp[2], r[1][2]) ^ multiply(temp[3], r[1][3])
        state[2][i] = multiply(temp[0], r[2][0]) ^ multiply(temp[1], r[2][1]) ^ multiply(temp[2], r[2][2]) ^ multiply(temp[3], r[2][3])
        state[3][i] = multiply(temp[0], r[3][0]) ^ multiply(temp[1], r[3][1]) ^ multiply(temp[2], r[3][2]) ^ multiply(temp[3], r[3][3])
        
    
    



    