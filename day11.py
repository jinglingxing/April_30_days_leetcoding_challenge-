#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 10:34:51 2020

@author: jinlingxing
"""

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            #calculate height of left and right subtrees
            h_left = self.height(root.left)
            h_right = self.height(root.right)
            # calculate the longest path without considering the root
            d_left = self.diameterOfBinaryTree(root.left)
            d_right = self.diameterOfBinaryTree(root.right)
            #no. edges = no.nodes - 1
            return max(h_left+h_right, max(d_left,d_right))
        
    def height(self, root):
        if root is None:
            return 0
        else:
            left = self.height(root.left)    
            right = self.height(root.right)
            return max(left,right)+1


        
        
if __name__ == "__main__":
#[1,2,3,4,5]
    tnode = TreeNode(1)
    tnode.left = TreeNode(2)
    tnode.right = TreeNode(3)
    tnode.left.left = TreeNode(4)
    tnode.left.right = TreeNode(5)
    sol = Solution()
    sol.diameterOfBinaryTree(tnode)