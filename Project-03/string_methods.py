x = "hello"
# count how many times
x.count('e')

#                                                                   ****
# Note: Strings are immutable(not changeable) datatypes
# lowercase (not changed the actual string in x)
x.lower()
# uppercase (not changed the actual string in x)
x.upper()

# Capitalize
x.capitalize()
#                                                                   ****
# capitalize the start of every word
x.title()
# Check bool
x.islower()
# space is number
x.isalpha()
x.isdigit()
# everything letter or number
x.isalnum()

# Others                                                             *****
x = "Happy Birthday"

# returns index or error if not found
x.index("Birthday")

# find like js returns index or -1 if not found
x.find("Birthday")
x.find("asdad")

x = "ff "
# only strip() removes "spaces"
x = x.strip()
# x = input("Name ?:")
# name with an extra space then it will caush extra len()
# x = input("Name ?:").strip()

# kind of trim (both side)
# x = x.strip("0")

# kind of trim (left side)
# x = x.lstrip("0")

# kind of trim (right side)
# x = x.rstrip("0")

print(len(x))