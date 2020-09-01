def merge_sort(A):
	if len(A)<=1:
		return A

	if len(A) == 2:
		if A[0]>A[1]:
			A[0], A[1] = A[1], A[0]

	s = 0
	e = len(A)
	mid = s + (e-s)//2
	A[:mid] = merge_sort(A[:mid])
	A[mid:] = merge_sort(A[mid:])
	A = merge_sorted_lists(A, s, mid, mid, e)
	return A

def merge_sorted_lists(A, s1, e1, s2, e2):
	B = [0] * len(A)
	k=0
	i1=s1
	i2=s2
	while i1<e1 and i2<e2:
		if A[i1] <= A[i2]:
			B[k] = A[i1]
			k += 1
			i1 += 1
		else:
			B[k] = A[i2]
			k += 1
			i2 += 1

	while i1 < e1:
		B[k] = A[i1]
		k += 1
		i1 +=1
	while i2 < e2:
		B[k] = A[i2]
		k += 1
		i2+= 1

	return B

assert(merge_sort([]) == [])
assert(merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5])
assert(merge_sort([10]) == [10])
assert(merge_sort([12, 10]) == [10, 12])
assert(merge_sort([8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8])
