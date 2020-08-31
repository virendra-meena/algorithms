def merge_two_sorted_lists(B, C, T):
	b=0
	c=0
	t=0
	
	while b<len(B) and c<len(C):
		if B[b]<=C[c]:
			T[t] = B[b]
			b+=1
			t+=1
		else:
			T[t] = C[c]
			c+=1
			t+=1

	if b<len(B):
		T[t:] = B[b:]
	
	if c<len(C):
		T[t:] = C[c:]
	
	return T	 

def merge_sort(A):
	if len(A) <= 1:
		return A
	
	if len(A) == 2:
		if A[0]>A[1]:
			A[0], A[1] = A[1], A[0]
		return A

	e = len(A)
	mid = e // 2
	
	B = merge_sort(A[:mid])
	C = merge_sort(A[mid:])
	
	A = merge_two_sorted_lists(B, C, A)
	return A

assert(merge_sort([]) == [])
assert(merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5])
assert(merge_sort([10]) == [10])
assert(merge_sort([12, 10]) == [10, 12])
assert(merge_sort([8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8])
