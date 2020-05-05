# range
# range( start, end, step(optional) )
'''
for i in range(1,10):
    # print(i)

for i in 'sdadasd':
    # print(i)

for i in '10':
    # print(i)

# find vowels and consonents in a sentence

vowel = 0
consonents = 0

for i in "aeiou t":
    if i in 'aeiou':
        vowel = vowel +1
    elif i == ' ':
        pass
    else:
        consonents = consonents +1

print(f'There are {vowel} vowels and {consonents} consonents')

'''
# loops over dictionaries

students = {
    "male": ['shovon', 'joy', 'asmit', 'avijit', 'ripon'],
    "female": ['shovona', 'joya', 'asmita', 'avijita', 'ripona'],
}

for key in students:
    for name in students[key]:
        # print(name)
        if 'a' in name:
            print(name)