class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        n = len(binary)
        j = 0
        for i in range(n):
            if binary[i] == '0':
                while j <= i or (j < n and binary[j] == '1'):
                    j += 1
                if j < n:
                    binary = binary[:j] + '1' + binary[j+1:]
                    binary = binary[:i] + '1' + binary[i+1:]
                    binary = binary[:i+1] + '0' + binary[i+2:]
        return binary