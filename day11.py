#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 10:34:51 2020

@author: Jinling Xing & Luc Michea
"""

'''
Problem:
    Given a binary tree, you need to compute the length of the diameter of 
    the tree. The diameter of a binary tree is the length of the longest 
    path between any two nodes in a tree. This path may or may not pass 
    through the root. 

Example :
    Given a binary tree 
          1
         / \ 
        2   3
       / \     
      4   5 

     Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: 
    The length of path between two nodes is represented by the number
    of edges between them. 
'''
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Our definition of a Tree
class Tree (object) :
    def __init__(self, inp_l: List[int] = []):
        if inp_l:
            inp = inp_l.copy()
            self.top = TreeNode(inp.pop(0))
            if inp :
                self.add_level([self.top],inp)
    
    def add_level(self, prev_lvl: List[TreeNode], inp_l: List[int]):
        lvl = []
        for prevN in prev_lvl:
            if inp_l :
                if len(inp_l) == 1:
                    prevN.left = TreeNode(inp_l.pop(0))
                    lvl.append(prevN.left)
                elif len(inp_l) > 1:
                    prevN.left = TreeNode(inp_l.pop(0))
                    lvl.append(prevN.left)
                    prevN.right = TreeNode(inp_l.pop(0))
                    lvl.append(prevN.right)
        
        if inp_l:
            self.add_level(lvl, inp_l)

    def str_lvl (self, prev_lvl: List[TreeNode], prev_node_pos: List[int] = [0]) -> str:
        line1 = ''
        line2 = ''
        lvl = []
        for i in range (len(prev_lvl)):
            prevN = prev_lvl[i]
            posN = prev_node_pos[i]
            
            # We check if we have the right spacing based on the position
            # of the previous node
            if len(line1) != 7*posN :
                line1 += ' '*7*(posN - (len(line1)%7))
                line2 += ' '*7*(posN - (len(line2)%7))

            if prevN.left.val:
                line1 += ' / '
                line2 += '{} '.format(prevN.left.val)
            else:
                line1 += '   '
                line2 += '   '
            if prevN.right.val:
                line1 += ' \ '
                line2 += '   {}'.format(prevN.right.val)
            else:
                line1 += '   '
                line2 += '   '
        return (line1 + '\n' + line2)

    def __str__ (self) -> str:
        l_str_lvl = self.str_lvl([self.top])

        return str(self.top.val)


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
    inp = [1,2,3,4,5]
    T = Tree(inp_l = inp)
    tnode = TreeNode(1)
    tnode.left = TreeNode(2)
    tnode.right = TreeNode(3)
    tnode.left.left = TreeNode(4)
    tnode.left.right = TreeNode(5)
    sol = Solution()
    out = sol.diameterOfBinaryTree(T.top)
    print("The solution to {} is : {}".format(inp, out))
    print('{}'.format(T))
    print(T.str_lvl([T.top]))