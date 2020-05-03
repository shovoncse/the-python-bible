# Ask for User Email adderss
email = input("Enter your Email: ").strip()

# Slice out username
username = email[:email.index("@")]

# slice domain name
domain = "www."+email[int(email.index("@")+1):]

# format message
output = "Your name is {} and your doamin name is {}".format(username, domain)

# Output 
print(output)