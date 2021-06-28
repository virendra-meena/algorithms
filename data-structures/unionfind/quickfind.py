class UF:
    def __init__(self, size):
        self.tree = [i for i in range(size)]

    def find(self, i):
        return self.tree[i]

    def connected(self, i, j):
        return self.find(i) == self.find(j)

    def union(self, i, j):	# i points to j, i.e. i is j's child
        p = self.find(i)
        q = self.find(j)

        for i in range(len(self.tree)):
            if self.find(i) == p:
                self.tree[i] = q