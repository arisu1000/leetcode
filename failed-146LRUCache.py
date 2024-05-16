#https://leetcode.com/problems/lru-cache

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LRUCache:
    capacity = 0
    cache = {}
    recentlyUsedOrder = ListNode(-1)    

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        recentlyUsedOrder = ListNode(-1)    

    def get(self, key: int) -> int:
        #사용 시간 업데이트하기
        try:
            self.cache[key]

            beforeTmp = ListNode(-1)
            tmp = self.recentlyUsedOrder

            # if tmp.val == -1:
            #     self.recentlyUsedOrder.val = key
            #     return self.cache[key]

            while tmp is not None:
                if tmp.val == key:
                    beforeTmp.next = tmp.next
                    if self.recentlyUsedOrder.val == -1:
                        self.recentlyUsedOrder = ListNode(key)
                    else:
                        self.recentlyUsedOrder = ListNode(key, self.recentlyUsedOrder)
                    break
                else:
                    beforeTmp = tmp
                    tmp = tmp.next

        except KeyError:
            return -1


        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if len(self.cache) == self.capacity:
            try:
               value = self.cache[key]
            except KeyError:
                #가장 사용한지 오래된 멤버를 지우고 새로운 값 추가하기
                beforeTmp = ListNode(-1)
                current = self.recentlyUsedOrder
                while current.next is not None:
                    beforeTmp = current
                    current = current.next
                
                if current.val != -1 :
                    del self.cache[current.val]
                    beforeTmp.next = None
                else:
                    del self.cache[beforeTmp.val]
                    beforeTmp.next = None
                    beforeTmp = None

                

                

                self.cache[key] = value
        else:
            self.cache[key] = value
            self.recentlyUsedOrder = ListNode(key, self.recentlyUsedOrder)

            # current = self.recentlyUsedOrder
            # while current.next is not None:
            #     current = current.next
            
            # current.next = ListNode(key)
            # current = current.next

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# s = LRUCache(2)
# s.put(2, 1)
# s.put(2, 2)
# print(s.get(2), 2)
# s.put(1, 1)
# s.put(4, 1)
# print(s.get(2), -1)


s = LRUCache(2)
s.put(1, 0)
s.put(2, 2)
print(s.get(1), 0)
s.put(3,3)
print(s.get(2), -1)
s.put(4,4)
print(s.get(1), -1)
print(s.get(3), 3)
print(s.get(4), 4)


s = LRUCache(2)
s.put(1, 1)
s.put(2, 2)
print(s.get(1), 1)
s.put(3,3)
print(s.get(2), -1)
s.put(4,4)
print(s.get(1), -1)
print(s.get(3), 3)
print(s.get(4), 4)

