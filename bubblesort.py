import pprint
pp = pprint.PrettyPrinter(indent=4)
import random
stuff = random.sample(range(1000000), 10000)
pp.pprint(stuff)
def bubble_sort(seq):
    changed = True
    while changed:
        changed = False
        for i in range(len(seq) - 1):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
                changed = True
        pp.pprint(seq)
    return None
bubble_sort(stuff)
