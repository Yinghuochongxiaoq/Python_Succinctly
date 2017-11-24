#!/usr/bin/env python3
print('hell freshMan')
sentce_in_double="He said,\"That's some greate tasting asparagus!\""
sentce_in_single='He sail,"That\'s some greate tasting asparagus!"'
a=sentce_in_single[0]
r=sentce_in_double[4]
print(a)
print(r)
vegetable_len=len(sentce_in_double)
print(vegetable_len)
print(sentce_in_double.lower())
print(sentce_in_single.upper())
print(sentce_in_double+' '+sentce_in_single)
print('-'*100)
print('Python '+str(10)+' is fun.')
print('Python {0} {1} and {1} {0} awesome!'.format('is',str(3)))
version=3
print('Python {} is fun.'.format(version))
print('-'*100)
print('{0:9} | {1:8}'.format('Vegetable','Quantity'))
print('{0:9} | {1:8}'.format('Asparagus',3))
print('{0:9} | {1:8}'.format('Online',10))

print('{0:9} | {1:<8}'.format('Vegetable','Quantity'))
print('{0:9} | {1:<8}'.format('Asparagus',3))
print('{0:9} | {1:<8}'.format('Online',10))

print('{0:9} | {1:^8}'.format('Vegetable','Quantity'))
print('{0:9} | {1:^8}'.format('Asparagus',3))
print('{0:9} | {1:^8}'.format('Online',20))

print('{0:8}|{1:<8}'.format('Vegetable','Quantity'))
print('{0:9}|{1:<8.2f}'.format('Aspragus',2.3553))
print('{0:9}|{1:<8.2f}'.format('Aspragus',2.3513))
print('{0:9}|{1:<8.2f}'.format('Online',10))

'''vegetable=input('Enter a name of a vegetable:')
print('{} is a lovely vegetable.'.format(vegetable))
'''

quantity_string='4'
total=int(quantity_string)+1
print(total)
print(float(total))
print(True)
false=False
print(false)

age = 103 
if age >= 35: 
    print('You are old enough to be a Representative, Senator, or the President.') 
elif age >= 30: 
    print('You are old enough to be a Senator.') 
elif age >= 25: 
    print('You are old enough to be a Representative.') 
else: 
    print('You are not old enough to be a Representative, Senator, or the President.') 
 
print('Have a nice day!')