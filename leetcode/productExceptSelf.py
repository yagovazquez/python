class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [None]*length
        a = 1
        b = 1

        for i in range(length):
            answer[i] = a
            a *= nums[i]

        for j in reversed(range(length)):
            answer[j] *= b
            b*= nums[j]

        return answer
