def quicksort(arr: list):
    if len(arr) < 2:
        return arr

    # choose mid as pivot and move it to end
    mid = len(arr) // 2
    end = len(arr) - 1
    arr[mid], arr[end] = arr[end], arr[mid]

    storage = 0     # storage points to index bigger than pivot
    pivot = arr[end]
    for i, num in enumerate(arr):
        if arr[i] < pivot:
            arr[i], arr[storage] = arr[storage], arr[i]
            storage += 1

    # move back pivot to right location
    arr[storage], arr[end] = arr[end], arr[storage]

    arr[:storage] = quicksort(arr[:storage])
    arr[storage+1:] = quicksort(arr[storage+1:])
    return arr


def test():
    arr = [1, 4, 3, 5, 8]
    print(quicksort(arr))


if __name__ == "__main__":
    test()
