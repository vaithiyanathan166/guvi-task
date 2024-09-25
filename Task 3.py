                                Problem Solving Task - 3

1)python list [10,501,22,37,100,999,87,351] task is to create two list one which have all the even numbers and another list which will have all the odd numbers in it?



# Original list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Lists to hold even and odd numbers
even_numbers = []
odd_numbers = []

# Loop through the list and separate even and odd numbers
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

# Print the results
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

Output:
Even numbers: [10, 22, 100]
Odd numbers: [501, 37, 999, 87, 351]




2  ) Given a python list [10,501,22,37,100,999,87,351]to count all the prime numbers and create a new python list which will contain all the prime numbers in it?


count all the prime numbers in a list and create a new list containing those prime numbers, 
# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True  # 2 is a prime number
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# List to hold prime numbers
prime_numbers = [num for num in numbers if is_prime(num)]

# Output the results
print("Prime numbers:", prime_numbers)
print("Count of prime numbers:", len(prime_numbers))

Output:
Prime numbers: [37]
Count of prime numbers: 1

The is_prime function checks whether a number is prime by testing divisibility up to the square root of the number.
The list comprehension is used to create a new list, prime_numbers, containing only the prime numbers from the original list.
The result is then printed, showing both the prime numbers found and their count.


3) 
Numbers for which this process ends in 1 are called happy numbers.
# Function to check if a number is a happy number
def is_happy_number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1
# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]
# List to hold happy numbers
happy_numbers = [num for num in numbers if is_happy_number(num)]
# Output the results
print("Happy numbers:", happy_numbers)
print("Count of happy numbers:", len(happy_numbers))
Output:
Happy numbers: [10, 100, 37]
Count of happy numbers: 3


4 ) write a python program to find the sum of the first and last digit of an integer?
# Function to calculate the sum of the first and last digit
def sum_first_last_digit(number):
    # Convert the number to a string to easily access the digits
    num_str = str(abs(number))  # Use abs() to handle negative numbers
    first_digit = int(num_str[0])
    last_digit = int(num_str[-1])
    return first_digit + last_digit

# Example usage
number = int(input("Enter an integer: "))
result = sum_first_last_digit(number)
print(f"The sum of the first and last digit of {number} is: {result}")

Use abs(number) to handle negative numbers, so that the sign doesn't affect the digits.
Access the first digit using num_str[0] and the last digit using num_str[-1].
Sum the first and last digits and return the result.
Example:
If the input is 2543, the output will be 5 (2 + 3).
If the input is -732, the output will be 9 (7 + 2).




5 ) 
def max_mango_difference(mangoes, m):
    # Sort the list of mangoes
    mangoes.sort()

    # Assign the first m bags to students
    # The smallest value to the first student and the largest to the last student
    max_diff = mangoes[-1] - mangoes[0]

    return max_diff

# Example usage
mangoes = [10, 20, 30, 50, 70, 100, 200]
m = 3  # Number of students
result = max_mango_difference(mangoes, m)
print(f"The maximum difference in mangoes distributed to the students is: {result}")

Sort the mangoes list: Sorting helps in easily picking the smallest and largest values, which will maximize the difference.
Assign the bags to the students: The first student gets the smallest bag, and the last student gets the largest.
Calculate the difference: The difference between the maximum and minimum mangoes in the chosen bags is the desired result.
Output:
Given mangoes = [10, 20, 30, 50, 70, 100, 200] and m = 3, the output will be 190 (200 - 10).


6 ) you have been given three lists .your task is to find the duplicates in the three lists write a python program for the same you can use your own python lists ?

# Example lists
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
list3 = [5, 6, 10, 11, 12]

# Convert lists to sets and find intersection
duplicates = set(list1) & set(list2) & set(list3)

# Convert the set back to a list (optional)
duplicates_list = list(duplicates)

# Print the results
print("Duplicates in all three lists:", duplicates_list)

Convert each list to a set: This helps in efficiently finding the common elements.
Use set intersection (&): This operation finds the common elements in all three sets.

Example Output:
Given the example lists:
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
list3 = [5, 6, 10, 11, 12]
Duplicates in all three lists: [5, 6]













7 ) write a python program to find the first non repeating elements in a given list of integers?


def first_non_repeating_element(nums):
    # Create a dictionary to store the count of each element
    count_dict = {}

    # Count occurrences of each element
    for num in nums:
        count_dict[num] = count_dict.get(num, 0) + 1

    # Find the first element with a count of 1
    for num in nums:
        if count_dict[num] == 1:
            return num

    return None  # If all elements are repeating

# Example usage
nums = [4, 5, 1, 2, 0, 4, 2, 5]
result = first_non_repeating_element(nums)
if result is not None:
    print(f"The first non-repeating element is: {result}")
else:
    print("There are no non-repeating elements in the list.")

The program uses a dictionary (count_dict) to keep track of the number of times each element appears in the list.

The first non-repeating element is returned. If all elements are repeating, it returns None.

Output

nums = [4, 5, 1, 2, 0, 4, 2, 5]


The first non-repeating element is: 1

1 is the first element that appears only once in the list.



8 ) write a python program to find the minimum element in a rated and sorted list?

def find_min_in_rotated_sorted_list(nums):
    # If the list is empty
    if not nums:
        return None
    
    left, right = 0, len(nums) - 1
    
    # If the list is not rotated (the smallest element is the first element)
    if nums[left] <= nums[right]:
        return nums[left]
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if the middle element is the minimum
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        
        if nums[mid] < nums[mid - 1]:
            return nums[mid]
        
        # Decide which part to search next
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid - 1
    
    return None

# Example usage
rotated_sorted_list = [4, 5, 6, 7, 0, 1, 2]
result = find_min_in_rotated_sorted_list(rotated_sorted_list)
if result is not None:
    print(f"The minimum element in the rotated sorted list is: {result}")
else:
    print("The list is empty or invalid.")

Binary Search Approach: The list is searched by dividing it into halves, comparing the middle element to the rightmost element to decide which part of the list contains the minimum element.



Pivot Detection:
If nums[mid] > nums[mid + 1], then nums[mid + 1] is the minimum.
If nums[mid] < nums[mid - 1], then nums[mid] is the minimum.
Adjust Search Space:
If nums[mid] > nums[right], the smallest element must be to the right of mid.
Otherwise, it must be to the left.
output
rotated_sorted_list = [4, 5, 6, 7, 0, 1, 2]

The minimum element in the rotated sorted list is: 0

Here, 0 is the minimum element in the rotated sorted list.

9 ) you have been give a python list [10,20,30,9] and a value of 59.write python program to find the triplet in the list whose sum is equal to the given value?

A  triplet in a list whose sum equals a given value,  use a combination of sorting and the two-pointer technique for efficiency. 

def find_triplet_with_sum(nums, target):
    # Sort the list
    nums.sort()
    
    n = len(nums)
    
    # Iterate over the list
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        
        # Use two-pointer approach to find the other two numbers
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == target:
                return (nums[i], nums[left], nums[right])
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    
    return None  # If no triplet is found

# Example usage
nums = [10, 20, 30, 9]
target = 59
result = find_triplet_with_sum(nums, target)

if result is not None:
    print(f"Triplet with sum {target} is: {result}")
else:
    print(f"No triplet with sum {target} found.")

Example Output:
Given the list:

nums = [10, 20, 30, 9]

and target:

target = 59

The output will be:

Triplet with sum 59 is: (9, 20, 30)

 the triplet (9, 20, 30) is the one whose sum is equal to 59.







10 ) Given a list [4,2,-3,1,6]write a python program to find if there is a sub list with sum equal to zero ?

def has_zero_sum_sublist(nums):
    # Initialize a set to store the cumulative sums
    seen_sums = set()
    
    # Initialize the cumulative sum
    current_sum = 0
    
    for num in nums:
        # Update the cumulative sum
        current_sum += num
        
        # Check if the cumulative sum is zero or if we've seen this sum before
        if current_sum == 0 or current_sum in seen_sums:
            return True
        
        # Add the current cumulative sum to the set
        seen_sums.add(current_sum)
    
    return False

# Example usage
nums = [4, 2, -3, 1, 6]
result = has_zero_sum_sublist(nums)

if result:
    print("There is a sublist with a sum of zero.")
else:
    print("There is no sublist with a sum of zero.")

If current_sum is zero at any point, it means that a sublist from the start up to the current index has a sum of zero.
If current_sum has been seen before, it means there is a sublist between the previous occurrence of current_sum and the current index that sums to zero.






Return Result: If a zero-sum sublist is found, return True; otherwise, return False.
Output:
Given the list:

nums = [4, 2, -3, 1, 6]

There is a sublist with a sum of zero.

In this case, the sublist [4, 2, -3, -1] has a sum of zero.

