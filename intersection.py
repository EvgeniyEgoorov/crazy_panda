import random
import timeit

from typing import List
from collections import Counter

"""
Formally the first option works faster, 
but it seems to me that first of all it was important to show an algorithmic solution.

So, I'd like to show both.

Here are the results I got on my box:
> Average find_intersection_v1 execution time (100 cycles):  0.126556 sec.
> Average find_intersection_v2 execution time (100 cycles):  0.146557 sec.
"""


def find_intersection_v1(a: List, b: List) -> List:
    intersection = list((Counter(a) & Counter(b)).elements())
    return intersection


def find_intersection_v2(a: List, b: List) -> List:
    match = {}
    for x in a:
        if x in match:
            match[x] += 1
        else:
            match[x] = 1
    intersection = []
    for x in b:
        if x in match:
            intersection.append(x)
            match[x] -= 1
            if match[x] == 0:
                del match[x]
    return intersection


def make_random_arr():
    return [random.randint(0, 1000) for _ in range(100000)]


def runtime_test(function) -> None:
    print(
        "Average {.__name__} execution time (100 cycles): {: f} sec.".format(
            function,
            timeit.timeit(
                lambda: function(make_random_arr(), make_random_arr()), number=100
            )
            / 100,
        )
    )


if __name__ == "__main__":
    # print(f'Intersection: {find_intersection_v1([1, 2, 3, 4, 4], [3, 4, 4, 5, 6])}')
    # print(f'Intersection: {find_intersection_v2([1, 2, 3, 4, 4], [3, 4, 4, 5, 6])}')
    runtime_test(find_intersection_v1)
    runtime_test(find_intersection_v2)
