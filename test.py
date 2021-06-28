class SegmentTree:
    def __init__(self, n, arr=None):
        self.n = n
        self.tree = [0] * 2*n

        self.tree[n:] = arr

        for i in reversed(range(1, self.n)):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]

    def update(self, index, val):
        index += self.n
        self.tree[index] = val

        index = index >> 1
        while index:
            self.tree[index] = self.tree[index << 1] + self.tree[index << 1 | 1]
            index = index >> 1


    def get_range_sum(self, start, end):    # end is not included
        start += self.n
        end += self.n

        ans = 0
        while start < end:
            if start & 1:
                start += 1
                ans += self.tree[start]

            if end & 1:
                ans += self.tree[end]
                end -= 1

            start = start >> 1
            end = end >> 1

        return ans
