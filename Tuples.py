months_of_year=('January','February','March','April','May','June','July','August','September','Octorber','November','December')
jan=months_of_year[0]
print(jan+'\n')
for month in months_of_year:
    print(month)

#months_of_year[0]='New January'

print(months_of_year)

#del months_of_year
#print(months_of_year)

months_of_year_list=list(months_of_year)
print('Months of the year tuple is {}'.format(type(months_of_year)))
print('Months of the year list is {}'.format(type(months_of_year_list)))

animals_list=['toad','lion','seal']
animals_tuple=tuple(animals_list)
print('Animals_list is {}'.format(type(animals_list)))
print('Animals_tuple is {}'.format(type(animals_tuple)))

(jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec)=months_of_year
print(jan)
print(feb)

contact_info=['5555-123','freshman']
(phone,email)=contact_info
print(phone)
print(email)

def high_and_low(numbers):
    '''Determin the highest and lowest number'''
    highest=max(numbers)
    lowest=min(numbers)
    return (highest,lowest)
lucky_numbers=[37,71,47,13,17,67]
(highest,lowest)=high_and_low(lucky_numbers)
print('The highest number is:{}'.format(highest))
print('The lowest number is:{}'.format(lowest))

contacts=[('David','5555'),('Tom','44444')]
for (name,phone) in contacts:
    print("{}'s hone number is {}".format(name,phone))

cities=[
    ('Short Hills,NJ','07078'),
    ('Fairfax Station,VA','22039'),
    ('Weston,CT','06883'),
    ('Great Falls,VA','22066')
]
for (city,zipCode) in cities:
    print('The ZIP code for {} is {}'.format(city,zipCode))