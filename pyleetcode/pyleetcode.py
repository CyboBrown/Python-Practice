class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        list = []
        for i, n in enumerate(nums):
            for j, m in enumerate(nums):
                # print("%d %d" %(n, m))
                if n + m == target and i != j:
                    list.append(i)
                    list.append(j)
                    break
            if len(list) > 0:
                break
        return list

# CODE
list = [1, 2, 3, 4]
print(Solution().twoSum(list, 7))