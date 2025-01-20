class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n,new_nums,length = len(nums),[],0
        dp = [[0] for _ in range(n)]
        for i in range(1,n):
            if nums[i] != nums[i-1]:
                new_nums.append(nums[i])
        m = len(new_nums)
        if m > 1:
            length = 2
            for i in range(1,m-1):
                if (new_nums[i]-new_nums[i-1])*(new_nums[i]-new_nums[i+1]) > 0:
                    length += 1
        else:
            length = 1
        return length