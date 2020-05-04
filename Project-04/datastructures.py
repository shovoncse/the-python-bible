# list
temp = [1,2,3,4,5]
temp = [1,[2,3,4,5],6,7,8]
table = [[1,2,3], [4,5,6], [7,8,9]]

temp.append(2)

# temp = temp + 2 # error
temp = temp + [2] # ok
temp = temp + list("BCD") # uncommon  
# temp = temp + list(123) # wrong        
temp = temp + list([123]) # right        
temp = temp + [[2,3,4]] # add a list inside list  
# insert
# temp = temp.insert(position, data)
temp = temp.insert(1, [34,234])

# print(temp)
# print(temp[-1])

# touples (imuteable/ unchangable datatype)

our_touple = 1,2,3,4,"A","B","C"

# print(our_touple)
# dictionaries

students = {
    'Alice': {'roll':1, 'class':3}, 
    'Bob': {'roll':2, 'class':2}, 
    'James': {'roll':3, 'class':1} 
    }

print(students['Alice']['roll'])

students = {
    'Alice': {'roll':1, 'class':3}, 
    'Bob': {'roll':2, 'class':2}, 
    'James': {'roll':3, 'class':1} 
    }

print(students['Alice']['roll'])


# sets
