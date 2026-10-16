#1.Find the Frequency of Each Word in a Sentence

def word_frequency(sentence):
    words = sentence.split()
    counts = {}

    for word in words:
       if word in counts:
        counts[word]+=1
       else:
        counts[word]=1

    return counts    

# 2.Find the Frequency of Each Character in a Word

def character_frequency(string):
    counts = {}

    for char in string:
       if char in counts:
          counts[char] += 1
       else:
          counts[char] = 1
    return counts

#Q3. Find the First Non-Repeating Character in a Word

def first_non_repeating(string):
    for char in string:
        if string.count(char) == 1:
            return char

    return None


# Q4. Check Whether Two Strings Are Anagrams

def are_anagrams(s1, s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False


# Q5. Find the First Repeating Character

def first_repeating(Text):
    characters = set()

    for char in Text:
        if char in characters:
            return char
        characters.add(char)

    return None

# Q6. Move All Zeros to the End of a List

def move_zeros(nums):
   result = []

   for num in nums:
      if num != 0:
         result.append(num)

   zero_count =len(nums) - len(result)
   result.extend([0]* zero_count)
        
   return result

# Q7. Find the Second Highest Distinct Number in a List

def second_highest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort(reverse=True)

    if len(unique_numbers) < 2:
        return None

    return unique_numbers[1]

# Q8. Remove Duplicates Without Changing the Original Order

def remove_duplicate(list):
   result = []

   for num in list:
      if num  not in result:
         result.append(num)

   return result     

# Q9. Find the Missing Number from 1 to N

def find_missing(numbers):
    n = len(numbers) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)

    return expected_sum - actual_sum
   

#Q10. Find Two Numbers Whose Sum Equals a Target

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] + nums[i] == target:
                return [nums[j], nums[i]]

    return []


# Q11. Find the Number Closest to Zero

def closest_to_zero(numbers):
    closest = numbers[0]

    for num in numbers:
        if abs(num) < abs(closest):
            closest = num
        elif abs(num) == abs(closest) and num > closest:
            closest = num

    return closest

#12.Find Common Elements Between Two Lists

def common_elements(list1, list2):
    result = []

    for num in list1:
        if num in list2 and num not in result:
            result.append(num)

    return result


# Q13. Rotate a List to the Right by K Positions

def rotate_right(nums, k):
    if len(nums) == 0:
        return nums

    k = k % len(nums)
    return nums[-k:] + nums[:-k] if k != 0 else nums

# Q14. Find the Maximum Sum of Two Consecutive Elements

def max_consecutive_sum(numbers):
    max = numbers[0] + numbers[1]

    for i in range(1, len(numbers) - 1):
        current_sum = numbers[i] + numbers[i + 1]

        if current_sum > max:
            max = current_sum

    return max

# Q15. Find All Pairs of Numbers Whose Sum Equals a Target

def find_all_pairs(nums, target):
    result = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pair = sorted([nums[i], nums[j]])

                if pair not in result:
                    result.append(pair)

    result.sort(key=lambda pair: pair[0])
    return result

