#['Hello', 'World', 'Huston', 'we', 'are', 'here'] should become -> ['World', 'Huston', 'we', 'are']
#['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'World']
#['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are', 'here']
#['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are']
#['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'Huston', 'are']
#['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['here', 'are', 'we', 'Huston', 'World', 'Hello']
#('Hello', 'World', 'Huston', 'we', 'are', 'here') should become -> ['World', 'Huston', 'we', 'are']
#'Hello World Huston we are here' -> 'World Huston we'

list = ['Hello', 'World', 'Huston', 'we', 'are', 'here']
print('TASK 1:', list[1:5])

print('TASK 2:', list[0:2])

print('TASK 3:', list[4::])

print('TASK 4:', list[4:-1])

print('TASK 5:', list[0:-1:2])

print('TASK 6:', list[::-1])

print('TASK 7:', list[::-1])

print('TASK 8:', list[1:-1])
print('TASK 8:', list[1:5])

print('TASK 9:', list[1:4])


# -1 tager sidste plads i arrayet
# [x:y] x er hvor vi vælger at starte i arrayet, og y er hvor vi vil slutte arrayet. 
# Dog eksluderer vi dette objekt og de efterfølgende objekter

