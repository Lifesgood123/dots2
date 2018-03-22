def factors(n):
    list = []
    for i in range(1, n+1):
        if n % i == 0:
            list.append(i)
    return list


def get_poss(a, c):
    possible_zeros = []

    for i in factors(c):
        for j in factors(a):
            possible_zeros.append(i/j)

    return possible_zeros

def guess(p, q):
    list = []
    for i in get_poss(p, q):
        if f(i) == 0:
            list.append(i)
        if f(-1*i) == 0:
            list.append(-i)

    return list        
