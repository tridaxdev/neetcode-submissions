class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            s = numbers[i] + numbers[j]
            if s == target:
                return [i+1, j+1]
            elif s < target:
                while numbers[i] == numbers[i+1]:
                    i+=1
                i+=1
            else:
                while numbers[j] == numbers[j-1]:
                    j-=1
                
                j-=1
        
            
        return []