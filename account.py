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
    return Details.find_detail(account)
