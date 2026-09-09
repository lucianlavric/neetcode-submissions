class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        for i in range(len(self.nums)):
            self.nums[i] *= -1
        heapq.heapify(self.nums)
        

    def add(self, val: int) -> int:
        # add integer
        heapq.heappush(self.nums, val * -1)
        print(self.nums)

        self.stack = []

        # find the kth largest
        # pop and add to stack
        for i in range(self.k - 1):
            num = heapq.heappop(self.nums)
            self.stack.append(num)
            print(self.nums)
        
        toReturn = self.nums[0] * -1 

        while self.stack:
            toAdd = self.stack.pop()
            heapq.heappush(self.nums, toAdd)

        # loop and readd to heap
        return toReturn



        # -3 -3 -3 -2 -1
        
