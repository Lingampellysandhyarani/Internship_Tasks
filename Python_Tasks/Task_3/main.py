# 1.word frequency
from solution import word_frequency

sentence = "python is easy and python is powerful"

result = word_frequency(sentence)

print(result)

#2. Character frequency 

from solution import character_frequency

string = "banana"

result = character_frequency(string)

print(result)

#Q3. Find the First Non-Repeating Character in a Word


from solution import first_non_repeating

print(first_non_repeating("swiss"))


from solution import are_anagrams

# Q4. Anagram Check
s1 = "listen"
s2 = "silent"
print(are_anagrams(s1, s2))

# 5.First repeating character

from solution import first_repeating

print(first_repeating("programming"))

#Q6. Move All Zeros to the End of a List

from solution import move_zeros

nums = [0, 3, 0, 1, 2, 0, 4]

result =  move_zeros(nums)

print(result)

## Q7.Find the Second Highest Distinct Number in a List

from solution import second_highest

numbers = [10, 20,40,30,40,20]

result = second_highest(numbers)

print(result)

# Q8. Remove Duplicates Without Changing the Original Order

from solution import remove_duplicate

list = [4,2,4,5,2,7,5]

result = remove_duplicate(list)

print(result)

#Q9. Find the Missing Number from 1 to N

from solution import find_missing

nums = [1, 2, 4, 5, 6]

result = find_missing(nums)

print(result)

#Q10. Find Two Numbers Whose Sum Equals a Target

from solution import two_sum

print(two_sum([2, 7, 11, 15], 9))


# Q11. Find the Number Closest to Zero

from solution import closest_to_zero

print(closest_to_zero([-8, -3, 2, 5, -2]))



# Q12. Find Common Elements Between Two Lists

from solution import common_elements 

print(common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))

# Q13. Rotate a List to the Right by K Positions

from solution import rotate_right

print(rotate_right([1,2,3,4,5],2))

# Q14. Find the Maximum Sum of Two Consecutive Elements

from solution import max_consecutive_sum

print(max_consecutive_sum([4, 7, 2, 9, 5]))


# Q15. Find All Pairs of Numbers Whose Sum Equals a Target

from solution import find_all_pairs

print(find_all_pairs([2, 4, 3, 5, 7, 8, 1],9))