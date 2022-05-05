"""
Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S.

In case of multiple subarrays, return the subarray which comes first on moving from left to right.



Example 1:

Input:
N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4
Explanation: The sum of elements
from 2nd position to 4th position
is 12.


Example 2:

Input:
N = 10, S = 15
A[] = {1,2,3,4,5,6,7,8,9,10}
Output: 1 5
Explanation: The sum of elements
from 1st position to 5th position
is 15.
"""


class Solution:
    def subArraySum(self,arr, n, s):
        # Write your code here
        Sum = 0
        start = 0
        end = 0
        while start < n:
            if(Sum == s):
                return [start+1, end]
            elif Sum > s:
                Sum -= arr[start]
                start = start + 1
            else:
                if end == n:
                    return [-1]
                Sum += arr[end]
                end = end + 1
        return [-1]

