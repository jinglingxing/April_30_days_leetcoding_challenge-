#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 09:23:18 2020

@author: jinlingxing
"""
from typing import List
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        left = 0
        right = 0
        for i in range(len(shift)):
            if shift[i][0] == 0:
                left += shift[i][1] 

            else:
                right += shift[i][1]               
        total_left = left-right
        if abs(total_left) > len(s):
            total_left = total_left%len(s)
        if total_left <= 0:
            s = s[total_left:] + s[:total_left]
        else:
            s = s[total_left:] + s[:total_left]
        return s
    
sol = Solution()
s = "xqgwkiqpif"
shift = [[1,4],[0,7],[0,8],[0,7],[0,6],[1,3],[0,1],[1,7],[0,5],[0,6]]
sol.stringShift(s, shift)

