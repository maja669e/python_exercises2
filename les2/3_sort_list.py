#Create a list of strings with names in it. (l = [‘Claus’, ‘Ib’, ‘Per’])
#Sort this list by using the sorted() build in function.
#Sort the list in reversed order.
#Sort the list on the lenght of the name.
#Sort the list based on the last letter in the name.
#Sort the list with the names where the letter ‘a’ is in the name first.

l = ['Claus', 'Alexander', 'Maja', 'August', 'Anna']
print('1. SORT LIST:', sorted(l))

print('2. REVERSED SORT LIST:', sorted(l, reverse=True))

print('3. LENGTH SORT LIST:', sorted(l, key=len))


def last_letter(word):
    return word[::-1]

print('4. LAST LETTER SORT LIST:', sorted(l, key=last_letter))



letter = 'a'
print('5. FIRST LETTER A SORT LIST:', sorted([i for i in l if i.lower().startswith(letter)]))



