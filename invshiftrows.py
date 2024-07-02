def rotate(word, n):
    return word[n:]+word[0:n]

def shiftRowsInv(state):
    for i in range(1,4):
        state[i] = rotate(state[i],-i)


