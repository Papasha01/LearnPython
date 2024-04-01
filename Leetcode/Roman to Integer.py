class Solution:
    def romanToInt(self, s: str) -> int:
        map = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        sum = 0
        while len(s) > 0:
            if len(s) > 1 and map[s[0]] < map[s[1]]:
                 sum += map[s[1]] - map[s[0]]
                 s = s[1:]
            else:
                sum += map[s[0]]
            s = s[1:]
        return sum
    
Sol = Solution()
print(Sol.romanToInt("MCMXCIV"))