contacts={'David':'3444424','Tom':'35456553454'}
davidphone=contacts['David']
tomphone=contacts['Tom']
print('Dial {} to call David.'.format(davidphone))
print('Dial {} to call Tom.'.format(tomphone))

contacts['Tom']='33333333'
print('Dial {} to call Tom.'.format(contacts['Tom']))

contacts['FreshMan']='95'
print(contacts)
print(len(contacts))

del contacts['David']
print(contacts)

contacts['Tom']=['123','456']
print(contacts)

for number in contacts['Tom']:
    print(number)

if 'Tom' in contacts.keys():
    print("Tom's phone number is:{}".format(contacts['Tom'][0]))

if ('Nora' in contacts.keys())==False:
    print('Nora not be included in dictionary')

print('95' in  contacts.values())

for contact in contacts:
    print("The number for {0} is {1}.".format(contact,contacts[contact]))

for person,personhone in contacts.items():
    print('The number for {0} is {1}.'.format(person,personhone))

contacts = { 
    'David': { 
        'phone': '555-0123', 
        'email': 'david@gmail.com' 
    }, 
    'Tom': { 
        'phone': '555-5678', 
        'email': 'tom@gmail.com' 
    } 
} 
 
for contact in contacts: 
    print("{}'s contact info:".format(contact)) 
    print(contacts[contact]['phone']) 
    print(contacts[contact]['email']) 