#Liquid Assets - PS0 A

def remove_vowel(string):
    vowels = ['a','e','i','o','u']
    result = [letter for letter in string if letter not in vowels]
    result = ''.join(result)
    print(result)
 
# Driver program
n = int(input())
string = input()
remove_vowel(string)
