class Solution(object):
    def singleNumber(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for i in arr:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1


        for i in arr:
            if count[i] == 1:
                return i

    