#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


# def eating_cookies(n, cache=None):
#     results = []
#     steps = [0, 1, 2, 3]
#     for i in range(n):
#         steps.append(steps[-1] + steps[-2] + steps[-3])
#         results.append(steps.pop(0))
#     return sum(results)+1

def eating_cookies(n, cache=None):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
