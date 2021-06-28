from heapq import heappop, heappush


class SequenceGenerator:
    def __init__(self):
        self.cache = []
        self.duplicate = set()
        self.min_heap = [(2, 2)]    # num, last_multiplier
        self.records = []

    def get_nth_entry(self, n):
        return self.compute(n)

    def compute(self, n):
        if n <= len(self.cache):
            return self.cache[n-1]

        # else compute
        while len(self.cache) < n:
            product, last_num = heappop(self.min_heap)
            self.cache.append(product)
            self.records.append((product, last_num))

            new_num = last_num + 1
            # generate next two numbers
            num1 = product * new_num
            num2 = last_num * new_num

            if num1 not in self.duplicate:
                heappush(self.min_heap, (num1, new_num))
                self.duplicate.add(num1)

            if num2 not in self.duplicate:
                heappush(self.min_heap, (num2, new_num))
                self.duplicate.add(num2)

        return self.cache[n-1]


generator = SequenceGenerator()


def solution(n):
    return generator.get_nth_entry(n)


def test():
    terms = [(1, 2), (2, 6), (4, 20), (5, 24)]
    for term, expected in terms:
        assert expected == solution(term)

def debug():
    solution(20)
    print(generator.cache)

#test()

debug()