print("Welcome to Mavis Restaurant!")
print("Kindly Login if you are a member or Register if you are not..")


user_details = {}
def for_user():
    user_input = input("Welcome! type 'Old' as a 'Old Member' or 'New' as a 'New Member': ").lower()
    if user_input == "new":
        register()
    elif user_input == "old":
        login()


def register():
    username = input("Input a username: ").lower()
    password = input("Input a password: ")
    if username not in user_details:
        user_details[username] = password
        print(user_details)
        print("=" * 60)
        print("Welcome %s to Mavis Restaurant..." %(username))
        login_question = input("Will you like to log in now type 'Yes' or 'No': ").lower()
        if login_question == "yes":
            login()
            print("=" * 60)
        elif login_question == "no":
            print("Thank you %s for Registering with Mavis Restaurants" %(username))


    else:
        print ("Username already exist!")
        print("=" * 60)
        register()

def login():
    username = input("Input your Username: ")
    password = input("Input your Password: ")
    if user_details[username] == password and username in user_details:
        print("Welcome %s, you are now Logged in..." %(username))
        print("=" * 60)

    elif username != password and username in user_details:
        print("Username and Password inputed does not match...")
        print("=" * 60)
        login()
    else:
        print("Invalid Input...")


