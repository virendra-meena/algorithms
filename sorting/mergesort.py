def merge(A: list, B: list) -> list:
    i, j, k = 0, 0, 0
    C = [0] * (len(A) + len(B))

    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            C[k] = A[i]
            i += 1
            k += 1
        else:
            C[k] = B[j]
            k += 1
            j += 1

    while i < len(A):
        C[k] = A[i]
        k += 1
        i += 1

    while j < len(B):
        C[k] = B[j]
        k += 1
        j += 1

    return C


def mergesort(arr: list) -> list:
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    A = mergesort(arr[:mid])
    B = mergesort(arr[mid:])

    C = merge(A, B)
    return C


def test():
    arr = [4, 5, 3, 7, 1]
    print(mergesort(arr))


if __name__ == "__main__":
    test()
