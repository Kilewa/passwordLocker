import random
import string
import pyperclip

class User:
    """
    Create User class that generates new instances of a user.

    """
    user_list = []

    def __init__(self, username, password):
        """
        method that defines the properties of a user.
        """
        self.username = username
        self.password = password
    def save_user(self):
        """
        A method that saves a new user instace into the user list
        """
        User.user_list.append(self)
    @classmethod
    def display_user(cls):
        return cls.user_list

    def delete_user(self):
        '''
        delete_account method deletes a  saved account from the list
        '''
        User.user_list.remove(self)
class Details():
        """
        Create details class to help create new objects of credentials
        """
        details_list = []
        @classmethod
        def verify_user(cls,username, password):
            """
            method to verify whether the user is in our user_list or not
            """   
            a_user = ""
            for user in User.user_list:
                if(user.username == username and user.password == password):
                        a_user == user.username
            return a_user
        def __init__(self,account,userName, password):
            """
            method that defines user Details to be stored
                """
            self.account = account
            self.userName = userName
            self.password = password  
        def save_details(self):
            """
            method to store a new details to the details list
            """
            Details.details_list.append(self)   
        def delete_details(self):
            """
            delete_details method that deletes an account details from the details_list
            """
            Details.details_list.remove(self)

        @classmethod
        def find_details(cls, account):
            """
            Method that takes in a account_name and returns a detail that matches that account_name.

            """
        @classmethod
        def copy_password(cls,account):
            found_details = Details.find_details(account)
            pyperclip.copy(found_details.password)    
    
        @classmethod
        def if_detail_exist(cls, account):
            """
            Method that checks if a detail exists from the credential list and returns true or false depending if the detail exists.
            """
            for detail in cls.details_list:
                if detail.account == account:
                    return True
            return False