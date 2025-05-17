'''
this project is useful for musicians looking
for an improvisation tool. will hopefully return
and add more functionality to this later.
maybe an app / GUI ?
'''

import random

major_keys = [ #defines the major keys we will pull later
    'A Major',
    'B Major',
    'C Major',
    'D Major',
    'E Major',
    'F Major',
    'G Major',
]

major_progressions = [ #defines the major progressions
    'I IV V vi',
    'I V vi IV',
    'vi IV I V',
    'I IV V',
    'I vi IV V',
    'I IV',
    'I V IV',
]

minor_keys = [ #defines the minor keys we will pull later
    'A Minor',
    'B Minor',
    'C Minor',
    'D Minor',
    'E Minor',
    'F Minor',
    'G Minor',
]

minor_progressions = [ #and our minor progressions
    'i vi v i',
    'i iv v i',
    'i bVII bVI bVII',
    'i vi III VII',
    'ii* v i'
]

#program that asks major or minor, and then one that supplies a random choice
user_input = str(input('Major or Minor? '))

def key_and_progression():
    if user_input == 'Major':
        print(random.choice(major_keys))
        print(random.choice(major_progressions))
    elif user_input == 'Minor':
        print(random.choice(minor_keys))
        print(random.choice(minor_progressions))
    else:
        print('Error! Please select again.')

print(user_input)
key_and_progression()