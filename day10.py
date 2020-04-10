#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 13:04:06 2020

@author: jinlingxing
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        minVal = self.stack[0]
        for i in range(0,len(self.stack)):
            if minVal > self.stack[i]:
                minVal = self.stack[i]
        return minVal


# Your MinStack object will be instantiated and called as such:
#["MinStack","push","push","push","getMin","pop","top","getMin"]
#[[],[-2],[0],[-3],[],[],[],[]]
        
obj = MinStack()
x = -2
obj.push(x)
x1 = 0
obj.push(x1)
x2 = -3
obj.push(x2)
p_0 = obj.getMin()
p_1 = obj.pop()
p_2 = obj.top()
p_3 = obj.getMin()

