from itertools import permutations

#Read in mathagram
mathagram = input()

#Collect a list of unused numbers
nums = list(range(1,10))
for c in list(mathagram):
    if c.isdigit():
        nums.remove(int(c))


#Collect a list of the indicies with an 'x'
puzzle_indices = []
for i,x in enumerate(mathagram):
    if x == "x":
        puzzle_indices.append(i)
    
        
#Run through every permutation of unused numbers until a solution is found
for i in permutations(nums, mathagram.count('x')):
    possible_answer = list(mathagram)
    for j,index in enumerate(puzzle_indices):
        possible_answer[index] = str(i[j])
    
    items = "".join(possible_answer).split(' ')
    items.remove("+")
    items.remove("=")
    if int(items[0]) + int(items[1]) == int(items[2]):
        print(items[0] + " + " + items[1] + " = " + items[2])
        break
