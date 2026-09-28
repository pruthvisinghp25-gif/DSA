class NumArray:

    def __init__(self, nums: list[int]):
        self.prfx = [0]

        for num in nums:
            self.prfx.append(self.prfx[-1] + num) 

    def sumRange(self, left: int, right: int) -> int:
        return self.prfx[right + 1] - self.prfx[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)