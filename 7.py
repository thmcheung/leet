class Solution:
    def reverse(self, x: int) -> int:
        a = str(x)
        a = a[::-1]
        if a[-1:] == '-':
            a = a[-1:] + a[:-1]
        if 2147483647 >= int(a) >= -2147483647:
            return int(a)
        else:
            return 0