class Solution:
    def reverse(self, x: int) -> int:
        if x <= -2 ** 31 or x >= 2 ** 31 - 1:
            return 0
        else:
            revr_x = int(str(x)[::-1] if x >= 0 else "-" + str(x)[1:][::-1])
            if revr_x <= -2 ** 31 or revr_x >= 2 ** 31 - 1:
                return 0
            else:
                return revr_x
y = 123
rev = Solution(y)
print (rev)