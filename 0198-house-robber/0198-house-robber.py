class Solution(object):
    def rob(self, nums):

        prev1, prev2 = 0, 0
        for num in nums:
            temp = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = temp
        return prev1
       
        