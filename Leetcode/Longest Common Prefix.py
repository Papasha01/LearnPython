class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        buffer = strs[0]
        for i in range(len(strs)):
            for j in range(len(buffer)):
                
                if buffer not in strs[i] or buffer != strs[i][:len(buffer)]:
                    buffer = buffer[:-1]
        return buffer
        
Sol = Solution()
print(Sol.longestCommonPrefix(["c","acc","ccc"]))