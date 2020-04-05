#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 16:01:58 2020

@author: jinlingxing & Luc
"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices)==0):
            return 0
        profit = 0
        for i in range(0,len(prices)-1):
            if(prices[i+1] - prices[i] > 0 ):
                profit += prices[i+1] - prices[i]
        return profit
        
if __name__ == "__main__" :       
    sol = Solution()
    prices = [7,1,5,3,6,4]
    sol.maxProfit(prices)
