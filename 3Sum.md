## 3Sum - Leet Code

## Problem 

<img width="646" alt="Screenshot 2024-04-23 at 12 46 04 PM" src="https://github.com/ssssubhank/Problem-Solving-Python/assets/99115039/00946936-9e42-4731-a59d-e226a7567be4">


## Solution

### Intuition and Approach 

1. **Initialization**: Similar to the two-sum problem, we'll use two pointers, 'left' and 'right', to iterate through the array. Additionally, we'll have an external loop where 'i' starts from 0 and the inner while loop runs with 'left' starting from 'i+1' and 'right' starting from 'n-1'. The termination condition for the inner loop is while 'left' is less than 'right'.

2. **Main Loop**: We calculate the target sum, which is 0 in this case, by adding 'nums[i]', 'nums[left]', and 'nums[right]'. If the target sum is found, we append the triplet to the answer list.

3. **Handling Duplicates**: To avoid duplicate triplets, we increment 'left' and decrement 'right'. Additionally, we run another loop to skip over duplicates for both 'left' and 'right'.

4. **Adjusting Pointers**: If the current sum is less than 0, we increase 'left'; otherwise, we decrease 'right'.

5. **Return**: Finally, we return the answer list containing all unique triplets whose sum is zero.


```python 

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()  # Sort the input list to simplify the solution

        # Iterate through the array
        for i in range(n - 2):
            # Skip duplicates to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1  # Initialize two pointers, 'left' and 'right'
            while left < right:
                # Calculate the current sum of three elements
                currsum = nums[i] + nums[left] + nums[right]
                
                # If the current sum is zero, add the triplet to the result
                if currsum == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    
                    # Move 'left' pointer to the right and 'right' pointer to the left
                    left += 1
                    right -= 1
                    
                    # Skip duplicates to avoid duplicate triplets
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                
                # If the current sum is less than zero, move 'left' pointer to the right
                elif currsum < 0:
                    left += 1
                
                # If the current sum is greater than zero, move 'right' pointer to the left
                else:
                    right -= 1
        
        return ans



```
