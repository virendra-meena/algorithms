"""
three optimizations of union and find data structure.


"""


class UF:
    def __init__(self, sz):
        self.sz = sz
        self.p = [i for i in range(sz)]
        self.sz = [1] * sz

    def root(self, i):
        while self.p[i] != i:
            self.p[i] = self.p[self.p[i]]
            i = self.p[i]

        return i

    def find(self, i):
        return self.root(i)

    def connected(self, i, j):
        return self.find(i) == self.find(j)

    def union(self, i, j):
        pi = self.find(i)
        pj = self.find(j)

        if pi == pj:
            return

        if self.sz[pi] > self.sz[pj]:
            self.p[pj] = self.p[pi]
            self.sz[pi] += self.sz[pj]
        else:
            self.p[pi] = self.p[pj]
            self.sz[pj] += self.sz[pi]


def test():
    uf = UF(10)
    print(uf.connected(1, 2))
    print(uf.union(1, 2))
    print(uf.connected(1, 2))


if __name__ == "__main__":
    test()