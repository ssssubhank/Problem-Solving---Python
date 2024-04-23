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
