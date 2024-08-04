class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarray_sums = []
      
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]  
                subarray_sums.append(current_sum)   
      
        subarray_sums.sort()
      
        mod = 10**9 + 7
      
        range_sum = sum(subarray_sums[left - 1 : right]) % mod
        return range_sum
