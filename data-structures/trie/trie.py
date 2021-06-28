import collections


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        def insert(node, word):
            if not word:
                node['#'] = word
                return

            c = word[0]
            if c not in node:
                node[c] = Trie()

            return insert(node[c], word[1:])

        return insert(self.root, word)

    def search(self, word):
        node = self.root
        for c in word:
            if c in node:
                node = node[c]
            else:
                return False

        if '#' in node:
            return True

        return False

    def starts_with(self, word):
        node = self.root
        for c in word:
            if c in node:
                node = node[c]
            else:
                return False

        return True


def test():
    t = Trie()
    items = ["banana", "kota", "delhi", "gurgaon", "bihar", "noida", "goa", "jaipur", "jodhpur"]
    for item in items:
        t.insert(item)

    assert True == t.search("kota")
    assert False == t.search("mumbai")
    assert True == t.starts_with("jodh")


if __name__ == "__main__":
    test()
