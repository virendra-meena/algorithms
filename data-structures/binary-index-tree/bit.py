class BIT:
    def __init__(self, arr):
        self.sz = len(arr) + 1
        self.tree = [0] * self.sz

        for i, n in enumerate(arr):
            self.add(i, n)

    def add(self, index, val):
        index += 1
        while index < self.sz:
            self.tree[index] += val
            index += index & -index

    def sum(self, index):
        total = 0
        index += 1
        while index > 0:
            total += self.tree[index]
            index -= index & -index

        return total


def test():
    arr = [i for i in range(10)]
    tree = BIT(arr)

    print(arr)
    print(tree.tree)

    res = tree.sum(8) - tree.sum(6)
    print(res)


if __name__ == "__main__":
    test()