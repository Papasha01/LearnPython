class Solution:
    def longestCommonPrefix(self, arr1: list, arr2: list) -> int:
        max_len = 0
        for i in arr1:
            while i>0:
                for j in arr2:
                    while j>0:
                        if str(i).startswith(str(j)) and max_len < len(str(j)):
                            max_len = len(str(j))
                            break
                        else:
                            j //= 10
                i //= 10
        return max_len

        
Sol = Solution()
print(Sol.longestCommonPrefix([1],12))