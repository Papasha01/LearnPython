nums = [-1234,-34,-9,-8,-7,-6,-5,-4,-2,-1,3,4,6,7,322,33245,34567,53476]
num = -3

low = 0
high = len(nums)-1

while low <= high:
      mid = (low+high)//2
      if nums[mid] == num:
            print(mid)
            break 
      
      elif nums[mid]>num:high = mid-1
      else: low = mid + 1