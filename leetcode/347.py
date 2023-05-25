from typing import List
from collections import defaultdict


"""
               10(0)
         8(1)          7(2)
    5(3)   6(4)     4(5)   3(6)
 1  2   3    4    5    6  7  8(14)
"""


def heap_pushpop(heap, node):
    heap[0] = node
    length = len(heap)
    idx = 0
    left = 2 * idx + 1
    while left < length:
        right = left + 1
        if right < length:
            smaller = left if heap[left][1] < heap[right][1] else right
        else:
            smaller = left
        if heap[idx][1] > heap[smaller][1]:
            heap[idx], heap[smaller] = heap[smaller], heap[idx]
            idx = smaller
            left = 2 * idx + 1
        else:
            break


def heap_push(heap, node):
    heap.append(node)
    idx = len(heap) - 1

    while idx > 0:
        p_idx = (idx - 1) // 2
        if heap[p_idx][1] > heap[idx][1]:
            heap[p_idx], heap[idx] = heap[idx], heap[p_idx]
            idx = p_idx
        else:
            break


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = defaultdict(int)
        for num in nums:
            num_counts[num] += 1

        heap = []  # List[Node]
        for num, count in num_counts.items():
            node = (num, count)
            length = len(heap)
            if length >= k:
                assert length == k
                root = heap[0]
                if node[1] > root[1]:
                    # print('pushpop', heap, node)
                    heap_pushpop(heap, node)
                else:
                    # print('continue', heap, node)
                    continue
            else:
                # print('push', heap, node)
                heap_push(heap, node)
        return [num for (num, _) in heap]


# print(Solution().topKFrequent([6,0,1,4,9,7,-3,1,-4,-8,4,-7,-3,3,2,-3,9,5,-4,0], 6))
