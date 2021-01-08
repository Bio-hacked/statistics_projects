#Code to find mean, median and mode

import math

ist1 = [1, 1, 2, 3, 4]



def MMM(ist1):
    Mean = sum(ist1) / len(ist1)
    Mode = max(sorted(ist1), key=ist1.count)
    Median = 0
    ist1.sort()

    if sum(ist1) % len(ist1) == 0:
        Median = ist1[round(len(ist1) / 2)] + ist1[math.floor(len(ist1 / 2))] / 2
    elif sum(ist1) % len(ist1) != 0:
        Median = ((ist1[round(len(ist1) / 2)]))

    return f"Mean = {Mean}, Median = {Median}, Mode = {Mode}"

print(MMM(ist1))
