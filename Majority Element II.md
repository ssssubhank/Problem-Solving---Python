# Majority Element II

## Problem

<img width="647" alt="Screenshot 2024-04-23 at 11 38 35 AM" src="https://github.com/ssssubhank/Problem-Solving---Python/assets/99115039/6a33f1c2-c3a5-42a4-9725-678328dc6177">



## Solution

This repository provides an intuitive explanation and implementation of the Majority Element Algorithm using Python, based on Moore's Voting Algorithm.

## Intuition

### Majority Element 1:
We utilize Moore's Voting Algorithm similar to the majority problem 1. Here's the intuitive approach:
1. **Traversing the List**: We traverse through the list.
2. **Counting Process**: We maintain a count and an element variable (`ele`). If the next element is the same as the current `ele`, we increase the count; otherwise, we decrement it. If the count reaches 0, we assign the current element to `ele` and continue with the process.
3. **Verification**: Finally, we verify if the element saved in `ele` is a majority by checking if its count is more than `n//2`. If yes, then it's the majority element.

[Detailed explanation and code implementation for Majority Element 1](https://leetcode.com/problems/majority-element/submissions/1193480677)

### Majority Element 2:
For majority element 2, we need to check whether an element appears more than `floor(n/3)` times. The process is similar to majority element 1, but this time we use two variables, `ele1` and `ele2`, and repeat the same process for both elements.

[Detailed explanation and code implementation for Majority Element 2](https://leetcode.com/problems/majority-element-ii/submissions/1193498682)

## Algorithm Implementation

```python

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Slight Changes to Moore's Voting Algorithm 
        count1 = 0 
        count2 = 0
        ele1 = None
        ele2 = None
        n = len(nums)

        # Applying Moore's Voting Algorithm
        for i in range(n):
            if count1 == 0 and ele2 != nums[i]:
                count1 = 1
                ele1 = nums[i]
            elif count2 == 0 and ele1 != nums[i]:
                count2 = 1
                ele2 = nums[i]
            elif nums[i] == ele1:
                count1 += 1
            elif nums[i] == ele2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        # Count occurrences of potential majority elements
        count11, count12 = 0, 0
        for i in range(n):
            if ele1 == nums[i]:
                count11 += 1
            if ele2 == nums[i]:
                count12 += 1

        # Initialize list to store majority elements
        ls = []
        mini = n // 3 + 1  # Minimum occurrence required for majority

        # Check if potential majority elements are actual majority elements
        if count11 >= mini:
            ls.append(ele1)
        if count12 >= mini:
            ls.append(ele2)

        # Uncomment the following line
        # if it is told to sort the answer array:
        # ls.sort()  # Time Complexity: O(2*log2) ~ O(1);

        return ls
```

## Usage

To use the Majority Element Algorithm, instantiate the `Solution` class and call the `majorityElement` method, passing the array as an argument.

```python
solution = Solution()
result = solution.majorityElement([3, 2, 3])
print(result)  # Output: [3]
```
