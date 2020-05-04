# Cinema Runinng list
cinema_status = {
    "Jungle Book": [12,10],
    "Jhon Wick": [18,10],
    "Inception": [12,10],
    "Batman Rises": [14,10],
    "Joker": [18,10]
}

while True:

    # Get user choice
    cinema = input("Which cinema are you want to watch?").strip().title()

    # check the avaiablity of the cinema
    if cinema in cinema_status:

        # check seat availablity
        if cinema_status[cinema][1] > 0:

            # get user age
            age = input("What is your age?:").strip()
            if age.isnumeric():

                if cinema_status[cinema][0] <= int(age):
                    print("Enjoy the Movie")
                    cinema_status[cinema][1] = cinema_status[cinema][1] - 1
                else:
                    print("This flim is not for you")
            else:
                print("Wrong age input")
        else:
            print("Sorry! we are sold out")

    else:
        print("Sorry! We don't have this one running")
    
    print(cinema_status)