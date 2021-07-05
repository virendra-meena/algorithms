"""
# Given m sticks with different lengths. Combine these sticks to form longer sticks with the same length. What's the smallest possible length of these newly unified sticks? Must use all sticks.
# m < 50
# max of single stick less than 20

# Example:
# Input: 5 2 1 5 2 1 5 2 1
# Output: 6
# (Process: 1+5, 1+5, 1+5, 2+2+2)
# ---------------------
# Input: 3 3 3 2 2 5
# Output: 9
# (Process: 3+3+3, 2+2+5)
# ---------------------
# Input: 1 2 3 4 5
# Output: 5
# (Process: 2+3, 1+4, 5)
# ---------------------
# Input: 1 3 4 5
# Output: 13
# (Process: 1+3+4+5)

clarifications
1. we can only combine one iteration?
(6, 6, 6, 6)

2. stick lengths are not unique
3. smallest possible length of these newly unified sticks.
4. can assume the are non-negative integers

constraints are-
1. m < 50.
2. 0 < arr[i] < 20


5 2 1 5 2 1 5 2 1

[5, 2+1+2, 5, 5, 2+1+1]

lo = max()
up = summazation --

divide the numbers intp k baskets of equal sum.
simplest solution
it is easy to form 1 group.-- just add them up.
if it is not odd, then I can actually form 2 groups.
if each group still not odd, then I can split them in

5 2 1 5 2 1 5 2 1
 [24]
[12] [12]  ->

total = k * sum(smallest)
| | | | |

to

521, 5
S[i-1, k]
S[i, k] =

24 = 2 * 12
24 = 3 * 8
24 = 4 * 6
24 = 8 * 3

1 2 3 4 6 8 12 24

sum = 6

verify([], 6)

X = [max([nums]), sum(nums)]
X = 5
24 = buckets * 5
25 = buckets * 6..


given a K=6, can we divide the array into equal partitions

nums = 5 2 1 5 2 1 5 2 1
       0 1.....i

i=0
k=0
[13], [2]


k = 6


S[i, k] = True,  if we can divide nums[1...i] into k groups.


S[i, k-1], S[i, k]

total = nums[1..i-1]


S[i, k] = S[i-1][k-1] and nums[i] == total/k-1
S



dfs(arr[1..m], k):


   # find collection of numbers with sum K.
   # call recursively on the remaining array to find K-1.
   if sum(arr) < total:
    return 0

   if sum(arr) == total:
      return 1

   if sum(arr) !=

   try to get collection of numbers that equals to total/k..===6


    dfs(arr[1..m], k-1)



dfs(a[], 3, 0):

  dfs(a, 3)


dfs(ar, groups, num):
    if num == 0:
       return True

    for each element in ar:
        required_sum = num-element
        binary_search
        dfs(ar, groups, num-element)

 nums = 5 2 1 5 2 1
 nums = 1/2 1/2 2 2 5 5

  1
  2
               dfs(1..m, 4, 6)

            dfs(2...m, 4, 1)
         dfs(3..m, 4, 0)  dfs(3..m, 3, 6)


dfs(map, k, required):
  if required_num in map:
     dfs(map-{required}, k-1, required=6)

  for n in map:
   if n<required:
        dfs(map-{num}, k, required-n)
"""


def main():
    pass
