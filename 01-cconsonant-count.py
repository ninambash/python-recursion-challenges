'''
Write a function that given a string, counts total number of consonants in it. 
A consonant is a English alphabet character that is not vowel (a, e, i, o and u). 
Examples of constants are b, c, d, f, g, ..
input will never have spaces or non letter characters

Examples: 

Input: 'snakes'
Output: 4

Input: 'SpamAndEggs'
Output: 8
'''
def count_consonants(string, index=0, count=0):
    vowels = "aeiouAEIOU"
    
    if index == len(string):
        return count
    elif string[index] not in vowels:
        count += 1
    
    return count_consonants(string, index + 1, count)
print(count_consonants("snakes")) # Output: 4
print(count_consonants("SpamAndEggs")) # Output: 8


