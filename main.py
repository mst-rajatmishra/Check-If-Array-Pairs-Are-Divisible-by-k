from typing import List

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_count = [0] * k
        
        # Count the occurrences of each remainder
        for num in arr:
            remainder = num % k
            # Adjust remainder to be positive
            if remainder < 0:
                remainder += k
            remainder_count[remainder] += 1
        
        # Check the pairs
        if remainder_count[0] % 2 != 0:
            return False
        
        for r in range(1, (k // 2) + 1):
            if r == k - r:  # This occurs only when k is even
                if remainder_count[r] % 2 != 0:
                    return False
            else:
                if remainder_count[r] != remainder_count[k - r]:
                    return False
        
        return True

# Example usage
solution = Solution()
print(solution.canArrange([1, 2, 3, 4, 5, 10, 6, 7, 8, 9], 5))  # Output: True
print(solution.canArrange([1, 2, 3, 4, 5, 6], 7))              # Output: True
print(solution.canArrange([1, 2, 3, 4, 5, 6], 10))             # Output: False
