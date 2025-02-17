"""
Take any indices from top and bottom, count how many mismatches 
TC: O(n)
SP: O(1)
"""
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check_common(target):
            bcount = 0
            tcount = 0
            for i in range(len(tops)):
                if tops[i] != target and bottoms[i] != target:
                    return -1
                if tops[i] != target:
                    tcount += 1
                if bottoms[i] != target:
                    bcount += 1
            return min(tcount, bcount)

        t = check_common(tops[0])
        if t == -1:
            return check_common(bottoms[0])
        return t
