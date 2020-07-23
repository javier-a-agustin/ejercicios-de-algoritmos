numero = -12340

class Solution:
    def reverse(self, x: int) -> int:
        new = ""
        x = str(x)
        if x[0] == '-':
            new = "-"
            x = x[1:]
        if x[len(x) - 1] == "0":
            x = x[:len(x) - 1]
        for l in range(len(x) - 1, -1, -1):
            new += x[l]
        return int(new)
        
solucion = Solution()

print(solucion.reverse(numero))