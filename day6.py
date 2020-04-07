#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 15:08:43 2020

@author: jinlingxing
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = []
        for i in strs:
            m = "".join(sorted(i))
            sorted_strs.append(m)
        strs_map = list(zip(sorted_strs, strs))
        res = {}
        for line in strs_map:
            if line[0] in res:
                res[line[0]].append(line[1])
            else:
                res[line[0]] = [line[1]]
        return res.values()