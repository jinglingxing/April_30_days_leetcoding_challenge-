#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 14:22:20 2020

@author: jinlingxing
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
import math
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        def list_size():
            count = 0
            curr = head
            while curr:
                count += 1
                curr = curr.next
            return count
        print(list_size())
        curr = head
        mid = math.ceil(list_size()/2)
        i = 0
        while curr :
            if i == mid:
                return curr
            i+=1
            curr = curr.next
        
    

if __name__=='__main__': 
  
    llist = ListNode(1) 
    #construct below list 
    # 1->12->1->4->1 
    llist.next = ListNode(4)
    llist.next.next =ListNode(1)
    llist.next.next.next = ListNode(12)
    llist.next.next.next.next = ListNode(1)
    sol = Solution()
    sol.middleNode(llist)
            
            