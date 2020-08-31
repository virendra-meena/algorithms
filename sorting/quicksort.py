def quicksort(A):
	if len(A) <= 1:	# already sorted.
		return A

	if len(A) == 2:	# easy to quickly sort by swapping.
		if A[0] > A[1]:
			A[0], A[1] = A[1], A[0]
		return A

	end = len(A)-1	
	A[0], A[end] = A[end], A[0]	# move the pivot to end
	
	left=0	# index to store smaller items
	right=0
	
	while right < end:
		if A[right] < A[end]:	# store it in left side of array using left index.
			A[right], A[left] = A[left], A[right]
			right += 1
			left += 1
		else:
			right += 1

	A[left], A[end] = A[end], A[left]	# move pivot to left slot.

	if left > 0:
		A[:left] = quicksort(A[:left])	# recursively sort left array

	if left != end:		# recursively sort right array
		A[left+1:] = quicksort(A[left+1:])

	return A

assert quicksort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert quicksort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert quicksort([3, 5, 2, 1, 4]) == [1, 2, 3, 4, 5]
assert quicksort([]) == []
assert quicksort([1, 2]) == [1, 2]
