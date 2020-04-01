#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 14:51:20 2020

@author: jinlingxing
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = {}
        for i in nums:
            if i not in res:
                res[i] = True
            else:
                res.pop(i)
        return list(res.keys()).pop()
    