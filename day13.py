#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 09:32:49 2020

@author: jinlingxing
"""
from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        max_len = 0
        dic = {}

        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                count -= 1
            if count == 0:
                max_len = i+1
            if count in dic:
                max_len = max(max_len, i - dic[count])
            else:
                dic[count] = i
        return max_len
sol = Solution()
nums = [0,0,1,0,0,0,1,1]
sol.findMaxLength(nums)