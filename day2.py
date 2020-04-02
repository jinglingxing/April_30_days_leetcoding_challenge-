#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 13:59:45 2020

@author: jinlingxing
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        n1 = str(n)
        res = 0
        res_list = []
        res_list.append(n)
        while res != 1:
            res = 0
            for i in n1:
                res = res + int(i) * int(i) 
            if res in res_list:
                return False 
            res_list.append(res)
            n1 = str(res)
        return True
            
sol = Solution()
n = 19
sol.isHappy(n)
