#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 11:26:21 2020

@author: jinlingxing
"""
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        for i in S:
            if i == '#' :
                s_idx = S.index(i)
                if s_idx == 0 :
                    S = S[1:]
                else :
                    S = S[0:s_idx-1]+S[s_idx+1:]
        for i in T:
            if i == '#' :
                t_idx = T.index(i)  
                if t_idx == 0:
                    T = T[1:]
                else:
                    T = T[0:t_idx-1]+T[t_idx+1:]
        
        if S == T:
            return True
        else:
            return False
            
if __name__ == "__main__":
    sol = Solution()
#    S = "ab##"
#    T = "c#d#"
    # S = "ab#c"
    # T = "ad#c"
    # S = "a#c"
    # T = "b"
    S = "a##c"
    T = "#a#c"
    sol.backspaceCompare(S, T)