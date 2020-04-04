#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:46:34 2020

@author: jinlingxing
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) > 0:
            dp = [nums[0]]*len(nums)
            for i in range(1, len(nums)):
                dp[i] = max(dp[i-1]+nums[i], nums[i])
            return max(dp)