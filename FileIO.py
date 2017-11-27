# hosts=open('readme.md')
# #hosts_file_contents=hosts.read()
# #print(hosts_file_contents)
# print('Current position:{}'.format(hosts.tell()))
# print(hosts.read())

# print('Current position :{}'.format(hosts.tell()))
# print(hosts.read())

# hosts.seek(0)
# #print('Current position:{}'.format(hosts.tell()))
# #print(hosts.read())

# print(hosts.read(4))
# print(hosts.tell())
# print('File closed? {}'.format(hosts.closed))
# if not hosts.closed:
#     hosts.close()
# print('File closed? {}'.format(hosts.closed))
print('Started reading the file.')
with open('readme.md') as hosts:
    print('File closed ?{}'.format(hosts.closed))
    print(hosts.read())
print('Finished reading the file.')
print('File closed? {}'.format(hosts.closed))

with open('readme.md') as hosts:
    for line in hosts:
        # print(line)
        print(line.rstrip())
        print(hosts.mode)
with open('file.txt','w') as the_file:
    the_file.write('This text will be written to the file.\n');
    the_file.write('Here is some more text.');

with open('img.jpg','rb') as pig_picture:
    pig_picture.seek(2)
    pig_picture.read(4)
    print(pig_picture.tell())
    print(pig_picture.mode)

unsorted_file_name = 'animals.txt' 
sorted_file_name = 'animals-sorted.txt' 
animals = [] 
try: 
    with open(unsorted_file_name) as animals_file: 
        for line in animals_file: 
            animals.append(line) 
    animals.sort() 
except: 
    print('Could not open {}.'.format(unsorted_file_name)) 
 
try:
    with open(sorted_file_name, 'w') as animals_sorted_file: 
        for animal in animals: 
            animals_sorted_file.write(animal) 
except:
    print('Could not open {}.'.format(sorted_file_name)) 

import sys
for path in sys.path:
    print(path)