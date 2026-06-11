class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s

        res = ""
        p = 2 * (numRows - 1)

        for i in range(numRows):
            for j in range(i, len(s), p):
                res += s[j]

                if i != 0 and i != numRows - 1 and j + p - 2*i < len(s):
                    res += s[j + p - 2*i]

        return res