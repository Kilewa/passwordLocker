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
        Details_list = []
        @classmethod
        def verify_user(cls,username, password):
            """
            method to verify whether the user is in our user_list or not
            """    
    