class Solution:
    def hammingWeight(self, n: int) -> int:
        ret=''
        while(n!=0):
            ret+=str(n%2)
            n//=2
        return ret
    
Sol = Solution()
print(Sol.hammingWeight(999))