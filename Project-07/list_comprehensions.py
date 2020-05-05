# othir
even_numbers = [x for x in range(1,101) if x% 2 == 0]
even_numbers = [[x] for x in range(1,101) if x% 2 == 0]
# define here...
# x is a variable
# print(even_numbers)

# finest example
words = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

answer = [[x] for x in words]
answer = [[x, x.upper(), x.lower()] for x in words]
answer = [[x, x.upper(), x.lower(), len(x)] for x in words]

print(answer)