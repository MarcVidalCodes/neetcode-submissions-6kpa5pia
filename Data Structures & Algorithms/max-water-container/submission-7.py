class Solution:
    def maxArea(self, heights: List[int]) -> int:
        curr_max = 0 
        l, r = 0, len(heights) - 1

        while l < r: 
            vol = (r - l) * min(heights[l], heights[r])

            if heights[r] >= heights[l]:
                l += 1
            else: 
                r -= 1

            curr_max = max(vol, curr_max)
        return curr_max