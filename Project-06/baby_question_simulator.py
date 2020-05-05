import random
from random import randint
from random import choice

questions = [
    'Why sky is blue?',
    'Why moon walks?',
    'Why humans die?',
    'Why did i come from?',
]

# ans = input(questions[random.randint(0,len(questions)-1)]).strip().lower()
# ans = input(questions[randint(0,len(questions)-1)]).strip().lower()
ans = input(choice(questions)).strip().lower()

while ans != 'idk':
    ans = input(f'Why {ans}? :').strip().lower()
    
    