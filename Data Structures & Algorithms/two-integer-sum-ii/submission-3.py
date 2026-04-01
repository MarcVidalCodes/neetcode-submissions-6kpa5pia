class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front = 0
        back = len(numbers) - 1

        while front < back: 
            summed = numbers[front] + numbers[back]

            if summed > target: 
                back -= 1
                continue
            elif summed < target: 
                front += 1
            else: 
                return [front + 1, back + 1]
            