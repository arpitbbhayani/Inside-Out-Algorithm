import random

from typing import List, Any


ELEMENTS = ['a', 'b', 'c', 'e', 'f', 'g', 'h']


def shuffle_io(arr: List[Any]) -> List[Any]:
  _sarr = []

  for i in range(len(arr)):
    # adding a space for one more element
    # in the shuffle array
    _sarr.append(None)

    # pick a random index in range [0, i]
    k = random.randint(0, i)

    # move element from kth position to ith position
    _sarr[i] = _sarr[k]

    # move arr[i] to kth index in shuffled array
    _sarr[k] = arr[i]

  # return the shuffled array
  return _sarr


print(shuffle_io(ELEMENTS))
