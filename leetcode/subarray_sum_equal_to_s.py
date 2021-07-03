import collections

from typing import List


class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        P = [0] * (len(A) + 1)
        for i in range(len(A)):
            P[i + 1] = P[i] + A[i]

            # A holds cumulative sum P[i….j] = P[j] - P[i]
            counter = collections.defaultdict(int)
            total = 0

        for i, p in enumerate(P):
            diff = p - S
            total += counter[diff]

            counter[p] += 1

        return total