#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 14:46:46 2020

@author: jinlingxing
"""
#Given an integer array arr, count element x such that x + 1 is also in arr.
#If there're duplicates in arr, count them seperately.
from typing import List
class Solution:
    def countElements(self, arr: List[int]) -> int:
        S = []
        count = 0
        for i in arr:
            S.append(i+1)
        for x in S:
            if x in arr:
                count += 1
        return count
        
        
        
if __name__ == "__main__":
    sol = Solution()
    arr = [1,3,2,3,5,0]
    sol.countElements(arr)