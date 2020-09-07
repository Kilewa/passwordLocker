from users import User, Details


def create_new_user(username,password):
    '''
    Function to create a new user with a username and password
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    Function to save a new user
    '''
    user.save_user()    
def display_user():
    """
    Function to display existing user
    """
    return User.display_user()      
def login_user(username,password):
    """
    function that checks whether a user exist and then login the user in.
    """
    check_user = Details.verify_user(username,password)
    return check_user

def create_new_detail(account,userName,password):
    """
    Function that creates new details for a given user account
    """
    new_detail = Details(account,userName,password)
    return new_detail

def save_detail(details):
    """
    Function to save details to the details list
    """
    details. save_details()
def display_accounts_details():
    """
    Function that returns all the saved details.
    """
    return Details.display_details()

def delete_detail(details):
    """
    Function to delete a details from details list

    """
    details.delete_details()  

def find_detail(account):
    """
    Function that finds a details by an account name and returns the details that belong to that account
    """
    return Details.find_details(account)

def check_details(account):
    """
    Function that check if a detail exists with that account name and return true or false

    """
    return Details.if_detail_exist(account)

def copy_password(account):
    """
    A funct that copies the password using the pyperclip framework
    We import the framework then declare a function that copies the emails.
    """
    return Details.copy_password(account)


def passWordLocker():
    print("Hello Welcome to PasswordLocker...\n Please enter one of the following to proceed.\n CA ---  Create New Account  \n LI ---  Have An Account  \n")
    short_code=input("").lower().strip()
    if short_code == "ca":
        print("Sign Up")
        print('*' * 50)
        username = input("User_name: ")
        while True:
            print(" TP - To type your own pasword:")
            password_Choice = input().lower().strip()
            if password_Choice == 'tp':
                password = input("Enter Password\n")
                break
            else:
                print("Invalid password please try again")
        save_user(create_new_user(username,password))
        print("*"*85)
        print(f"Hello {username}, Your account has been created succesfully! Your password is: {password}")
        print("*"*85)
    elif short_code == "li":
        print("*"*50)
        print("Enter your User name and your Password to log in:")
        print('*' * 50)
        username = input("User name: ")
        password = input("password: ")
        login = login_user(username,password)
        if login_user == login:
            print(f"Hello {username}.Welcome To PassWord Locker Manager")  
            print('\n')
    while True:
        print("Use these short codes:\n CD - Create a new Detail\n DD - Display Details \n FD - Find a Detail\n GP - Generate A randomn password \n D - Delete credential \n EX - Exit the application \n")
        short_code = input().lower().strip()
        if short_code == "cd":
            print("Create New Detail")
            print("."*20)
            print("Account name ....")
            account = input().lower()
            print("Your Account username")
            userName = input()
            while True:
                print(" TP - To type your own pasword if you already have an account: ")
                password_Choice = input().lower().strip()
                if password_Choice == 'tp':
                    password = input("Enter Your Own Password\n")
                    break
                else:
                    print("Invalid password please try again")
            save_detail(create_new_detail(account,userName,password))
            print('\n')
            print(f"Account Details for: {account} - UserName: {userName} - Password:{password} created succesfully")
            print('\n')
        elif short_code == "dd":
            if display_accounts_details():
                print("Here's your list of accounts: ")
                
                print('*' * 30)
                print('_'* 30)
                for account in display_accounts_details():
                    print(f" Account:{account.account} \n User Name:{username}\n Password:{password}")
                    print('_'* 30)
                print('*' * 30)
            else:
                print("You don't have any details saved yet..........")
        elif short_code == "fd":
            print("Enter the Account Name you want to search for")
            search_name = input().lower()
            if find_detail(search_name):
                search_detail = find_detail(search_name)
                print(f"Account Name : {search_detail.account}")
                print('-' * 50)
                print(f"User Name: {search_detail.userName} Password :{search_detail.password}")
                print('-' * 50)
            else:
                print("That Detail does not exist")
                print('\n')
        elif short_code == "d":
            print("Enter the account name of the Details you want to delete")
            search_name = input().lower()
            if find_detail(search_name):
                search_detail = find_detail(search_name)
                print("_"*50)
                search_detail.delete_details()
                print('\n')
                print(f"Your stored details for : {search_detail.account} successfully deleted!!!")
                print('\n')
            else:
                print("That Detail you want to delete does not exist  in database")
        elif short_code == 'ex':
            print("Thanks for using passwords Database.. See you next time!")
            break
        else:
            print("Wrong entry... Check your entry again and let it match those in the menu")
    else:
        print("Please enter a valid input to continue")

if __name__ == '__main__':
    passWordLocker()
