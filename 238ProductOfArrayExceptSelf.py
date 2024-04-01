#https://leetcode.com/problems/product-of-array-except-self

#TODO: 다시 풀어봐야함.

from typing import List

# 내가 푼거
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         length = len(nums)
#         result = []

#         for i in range(length):
#             innerProduct = 1
#             for j in range(length):
#                 if i != j:
#                     innerProduct *= nums[j]
            
#             result.append(innerProduct)
        
#         return result


#풀이 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n  # 결과 배열을 1로 초기화

        # 왼쪽 누적 곱 계산
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]

        # 오른쪽 누적 곱을 계산하며 최종 결과를 answer에 바로 업데이트
        right_product = 1
        for i in range(n-1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer

s = Solution()
print(s.productExceptSelf([1,2,3,4]))
print(s.productExceptSelf([-1,1,0,-3,3]))