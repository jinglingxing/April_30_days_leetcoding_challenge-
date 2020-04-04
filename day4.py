#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:39:24 2020

@author: jinlingxing
"""
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-1
        while i >= 0:
            if(nums[i] == 0):
                nums.pop(i)
                nums.append(0)
            i-=1
        return nums
    
sol = Solution()
nums = [0,0,1,2,0,12]
sol.moveZeroes(nums)