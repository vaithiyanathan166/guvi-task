                                         PROBLEM SOLVING Task -- 2

1)To write a Python program that calculates the total number of vowels and counts the occurrences of each individual vowel (a, e, i, o, u) in a given string, 
def count_vowels(s):

    # Initialize a dictionary to hold the count of each vowel
    vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    # Initialize a variable to keep track of the total number of vowels
    total_vowels = 0
    
    # Convert the string to lowercase to handle both uppercase and lowercase vowels
    s = s.lower()
    
    # Iterate through each character in the string
    for char in s:
        if char in vowel_counts:
            vowel_counts[char] += 1
            total_vowels += 1
    
    return total_vowels, vowel_counts

# Input string
input_string = input("Enter a string: ")

# Get the total number of vowels and the count of each vowel
total_vowels, vowel_counts = count_vowels(input_string)

# Print the results
print(f"Total number of vowels: {total_vowels}")
print("Count of each vowel:")
for vowel, count in vowel_counts.items():
    print(f"{vowel}: {count}")


2 ) create a pyramid of numbers from 1 to 20 using a For  loop

def print_number_pyramid(n):
    current_number = 1
    for i in range(1, n+1):
        # Print spaces for pyramid alignment
        print(' ' * (n - i), end='')
        
        # Print numbers in the current row
        for j in range(i):
            if current_number <= n:
                print(current_number, end=' ')
                current_number += 1
        print()  # Move to the next line

# Print a pyramid with numbers from 1 to 20
print_number_pyramid(20)

 







3 ) To write a program that takes a string and returns a new string containing only the vowels, 

def extract_vowels(input_string):
    # Define the set of vowels (both uppercase and lowercase)
    vowels = "aeiouAEIOU"
    
    # Use a list comprehension to filter out the vowels
    result = ''.join([char for char in input_string if char in vowels])
    
    return result

# Example usage
input_string = "Hello, World!"
vowel_string = extract_vowels(input_string)
print("Original string:", input_string)
print("Vowel string:", vowel_string)


4)write a program that takes a string returns a number of unique characteres in it

def count_unique_characters(input_string):
    # Use a set to store unique characters
    unique_characters = set(input_string)
    
    # Return the number of unique characters
    return len(unique_characters)

# Example usage
input_string = "Hello, World!"
unique_count = count_unique_characters(input_string)
print("Original string:", input_string)
print("Number of unique characters:", unique_count)

This will output:

Original string: Hello, World!
Number of unique characters: 10

The unique characters are: 'H', 'e', 'l', 'o', ' ', ',', 'W', 'r', 'd', '!'.


5)write a program that takes a string returns True if it is a palindrome ,false otherwise

A palindrome is a string that reads the same forwards and backwards. 

def is_palindrome(input_string):
    # Remove spaces and convert to lowercase for uniform comparison
    cleaned_string = ''.join(input_string.split()).lower()
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]

# Example usage
input_string = "A man a plan a canal Panama"
result = is_palindrome(input_string)
print("Original string:", input_string)
print("Is palindrome:", result)

 For instance:

"racecar" should return True.

"hello" should return False.


6)write a program that takes a two string returns the longest common substring between them 
    # Initialize a 2D list with zeros
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Variables to keep track of the length and end index of the longest common substring
    longest = 0
    end_index_s1 = 0

    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                # Update the longest common substring length and its end index
                if dp[i][j] > longest:
                    longest = dp[i][j]
                    end_index_s1 = i
            else:
                dp[i][j] = 0

    # Extract the longest common substring using the length and end index
    longest_common_substr = s1[end_index_s1 - longest:end_index_s1]
    return longest_common_substr

# Example usage
s1 = "ABCXYZAY"
s2 = "XYZABCD"
longest_substring = longest_common_substring(s1, s2)
print("Longest common substring:", longest_substring)


7)write a program that takes a string and returns the most frequent character on it

    # Count the frequency of each character using Counter
    frequency = Counter(s)
    
    # Find the character with the highest frequency
    most_frequent = max(frequency, key=frequency.get)
    
    return most_frequent

# Example usage
input_string = "programming"
most_frequent = most_frequent_character(input_string)
print("The most frequent character is:", most_frequent)





9)write a program that takes a string and returns the number words in it

def count_words(input_string):
    # Split the string into words based on whitespace
    words = input_string.split()
    # Return the number of words
    return len(words)

# Example usage:
input_string = "GUVI."
word_count = count_words(input_string)
word_count


https://github.com/vaithiyanathan166/vaithiyanathan.git