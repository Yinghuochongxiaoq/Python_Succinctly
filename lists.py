animals=['toad','lion','seal']
print(animals[0])
print(animals[2])
print(animals.__len__())
animals[0]='sheep'
print(animals[0])
print(animals[-1])
print(animals[-2])
animals.append('fox')
print(animals[-1])
animals.extend(['owl','check','duck'])
print(animals)

more_animals=['whale','elk']
animals.extend(more_animals)
print(animals)

animals.insert(-1,'whale')
animals.insert(90,'Person')
print(animals)

some_animals=animals[1:4]
print(some_animals)
first_two=animals[0:2]
print(first_two)

first_two_again=animals[:2]
print(first_two_again)

last_two=animals[4:6]
print(last_two)

last_two_again=animals[-2:]
print(last_two_again)

part_of_a_whale='whale'[1:3]
print(part_of_a_whale)

lion_index=animals.index('lion')
print(lion_index)

try:
    non_index=animals.index('Fresh')
except:
    non_index=-1
print(non_index)

for animal in animals:
    print(animal.upper())

index=0
while index <len(animals):
    print(animals[index])
    index+=1

sorted_animals=sorted(animals)
print('Animal list:{}'.format(animals))

print("Sorted animals list:{}".format(sorted_animals))
animals.sort()
print("Animals after sort method:{}".format(animals))

all_animals=animals+more_animals
print(all_animals)

for number in range(4):
    print(number)

for number in range(2,6):
    print(number)

for number in range(0,10,5):
    print(number)



