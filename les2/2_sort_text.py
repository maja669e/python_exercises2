#Create a function that takes a string as a parameter and returns a list.
#The function should remove all vowels and sort the consonants in alphabetic order, 
# and the return the result.

def rem_vowel(string):
    vowels = ['a','e','i','o','u', 'y']
    result = [letter for letter in string if letter.lower() not in vowels]
    #Vi overskriver vores gamle result, med en ny result string
    #Result = Den sætning vi inputter
    result = ''.join(sorted(result))
    print(result)
 
# Driver program
string = "Python is funita"
rem_vowel(string)

string = 'Test'
