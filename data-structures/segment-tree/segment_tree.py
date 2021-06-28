class SegmentTree:
    def __init__(self, arr):
        self.sz = len(arr)
        self.tree = [0] * (self.sz * 2)

        for i in range(len(arr)):
            self.tree[self.sz + i] = arr[i]

        for i in reversed(range(1, len(arr) - 1)):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]

    def update(self, index, val):
        index = self.sz + index
        self.tree[index] = val
        index = index // 2
        while index:
            self.tree[index] = self.tree[2*index] + self.tree[2*index+1]
            index = index // 2

    def get_range(self, start, end):     # [start, end)
        start += self.sz
        end += self.sz

        total = 0
        while start < end:
            if start & 1:     # odd index
                total += self.s[start]
                start += 1

            if end & 1:
                end -= 1
                total = self.tree[end]

            start = start // 2
            end = end // 2

        return total
