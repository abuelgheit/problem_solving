class Solution:
    def reverse(self, x):
        s = str(x)

        if "-" in s:
            s = int("-" + ''.join(s[::-1])[:-1])
            if s < -2147483647 :
                #print("0")
                return 0
            else:
                #print(s)
                return s
        else:
            s = int(''.join(s[::-1]))
            if s > 2147483647 :
                #print("0")
                return 0
            else:
                #print(s)
                return s

