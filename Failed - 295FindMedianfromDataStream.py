# https://leetcode.com/problems/find-median-from-data-stream

import heapq

class MedianFinder:

    data = []

    def __init__(self):
        # 최대 힙과 최소 힙을 초기화
        self.left_half = [] # 최대 힙(음수로 저장해 최대값이 루트에 오도록 함)
        self.right_half = [] # 최소 힙


    def addNum(self, num: int) -> None:
        # 최대 힙에 새로운 숫자를 추가 (음수로 저장하여 최대 힙처럼 동작하게 함)
        heapq.heappush(self.left_half, -num)

        # 최대 힙의 최대값이 최소 힙의 최소값보다 커지면 안됨
        if self.left_half and self.right_half and (-self.left_half[0] > self.right_half[0]):
            val = -heapq.heappop(self.left_half)
            heapq.heappush(self.right_half, val)
        
        # 두 힙의 크기를 균형 있게 유지
        if len(self.left_half) > len(self.right_half) + 1:
            val = -heapq.heappop(self.left_half)
            heapq.heappush(self.right_half, val)
        elif len(self.right_half) > len(self.left_half):
            val = heapq.heappop(self.right_half)
            heapq.heappush(self.left_half, -val)


    def findMedian(self) -> float:
        # 원소의 개수가 홀수일 때는 최대 힙의 루트 값이 중간값
        if len(self.left_half) > len(self.right_half):
            return -self.left_half[0]
        # 원소의 개수가 짝수일 때는 두 힙의 루트 값의 평균이 중간값
        return (-self.left_half[0] + self.right_half[0]) / 2.0
    

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


medianFinder = MedianFinder();
medianFinder.addNum(1);  
medianFinder.addNum(2);  
print(medianFinder.findMedian())
medianFinder.addNum(3);  
print(medianFinder.findMedian())