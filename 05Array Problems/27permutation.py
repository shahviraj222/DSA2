# permutation the element postions is better.

#problem 1: generate all permutation 

# intution :
# see this as decision tree 
#  ⚙️ Optimal Approach → Backtracking
# 👉 Backtracking (Swap method or Used-array method)
# Time complexity is O(n!)


# problem 2 : find the next number in array according to dictionary order
# https://www.youtube.com/watch?v=JDOXKqF60RQ


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        index = -1
        # find index longest prefix
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                index = i
        # find the bigger the ith but smallest
        min = float("inf")
        minindex = -1
        for i in range(index,len(nums)):
            if nums[i]>nums[index]:
                if min > nums[i]:
                    min = nums[i]
                    minindex = i

        # swap elements
        nums[minindex],nums[index] = nums[index], nums[minindex]
        
        # sort the element from i+1 index to the len(nums)
        nums[index+1:] = sorted(nums[index+1:])



        