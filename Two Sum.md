# Two Sum

## Problem 

<img width="646" alt="Screenshot 2024-04-23 at 12 18 35 PM" src="https://github.com/ssssubhank/Problem-Solving---Python/assets/99115039/6a720b41-455f-463d-8634-0bd8d966bbca">


## Solution 
**Intuition:**

1. **Initialization**: We start by setting two pointers, 'left' and 'right', to the first and last indices of the array, respectively. These pointers will help us iterate through the array.

2. **Sorting with Indices**: To preserve the original indices of the elements, we sort the array along with its indices. This sorting ensures that we can track the positions of the elements in the original array even after sorting.

3. **Main Loop**: We enter a loop where we calculate the sum of the elements at the 'left' and 'right' pointers. 

4. **Comparison with Target**: If the sum equals the target, we have found the two numbers that add up to the target, and we return their indices. If the sum is less than the target, it means we need to increase the sum, so we move the 'left' pointer to the right to consider a larger element. If the sum is greater than the target, it means we need to decrease the sum, so we move the 'right' pointer to the left to consider a smaller element.

5. **Termination**: We continue this process until the 'left' pointer surpasses the 'right' pointer. If no such pair is found that sums up to the target, we return an empty list.

By sorting the array and maintaining two pointers, we can efficiently find the indices of the two numbers that add up to the target.


## Code

```python
class Solution:
    def twoSum(self, nums, target):
        nums_with_indices = list(enumerate(nums))

        nums_with_indices.sort(key=lambda x: x[1])  # Sort by values

        left, right = 0, len(nums) - 1

        while left < right:
            current_sum = nums_with_indices[left][1] + nums_with_indices[right][1]

            if current_sum == target:
                return [nums_with_indices[left][0], nums_with_indices[right][0]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        return []

```
