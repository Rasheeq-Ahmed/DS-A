
'''
Overview
Two Sum: find if any two numbers in input array add up to target

Strategy:
Create a hash to keep track of numbers you have seen
Iterate over the array
Create variable for a complementary number for current iteration
Check if that complement is available in hash
If the complement already exists already means it's a number we've seen
Return current num and complement
Otherwise finish iterating through the array 
Return empty array if no pair found

Time Complexity: O(n) where n is the length of the array
Space Complexity: O(n) where n is the length of the array
'''



def twoSum(array,target):
    seenNumbers = {}
    for num in array:
        complement = target - num
        if complement in seenNumbers:
                return [num, complement]
        else:
            seenNumbers[num] = True
    return []


assert twoSum([3, 5, -4, 8, 11, 1, -1, 6], 10) == [-1, 11]
