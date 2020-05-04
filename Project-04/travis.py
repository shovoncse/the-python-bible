known_user = ['Alice', 'Bob', 'Shovon', 'Joy', 'Pappu', 'Lopa', 'Brad']

while True:
    print('Hi, My name is Travis')
    name = input('What is your name? :').strip().capitalize()

    if not name.isalpha():
        continue

    if name in known_user:
        print(f'Hello {name}, you are a listed member')
        answer = input("Do you want to be removed from the list (y/n)?:").lower()

        if answer == 'y':
            known_user.remove(name)

        elif answer == 'n':
            print("No problem, I didn't want you to leave anyway!")

    else:
        print(f'Hello {name}, you are not a listed member')
        answer = input("Do you want to be our listed member (y/n)?:").lower()

        if answer == 'y':
            known_user.append(name)

        elif answer == 'n':
            print("No worries, see you around!")