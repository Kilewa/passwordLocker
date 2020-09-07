import unittest
from users import User
from users import Details


class TestClass(unittest.TestCase):
    """
    A Test class that defines test cases for the User class.
    """
    def setUp(self):
        """
        Method that runs before each individual test methods run.
        """

        self.new_user = User('GeorgeKilewa','StAiGhTOrSyoki@#@&')

    def test_init(self):
        """
        test case to chek if the object has been initialized correctly
        """
        self.assertEqual(self.new_user.username,'GeorgeKilewa')
        self.assertEqual(self.new_user.password,'StAiGhTOrSyoki@#@&')
    def test_save_user(self):
        """
        test case to test if a new user instance has been saved into the User list

        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1) 

class TestDetails(unittest.TestCase):
    """
    A test class that defines test cases for details class

    """ 
    def setUp(self):
        """
        Method that runs before each individual details test methods run.

        """
        self.new_detail = Details('Facebook','KilewaGeorge','StAiGhTOrSyoki@#@&')
    def test_init(self):
        """
        Test case to check if a new Details instance has been initialized correctly
        """
        self.assertEqual(self.new_detail.account,'Facebook')
        self.assertEqual(self.new_detail.userName,'KilewaGeorge')
        self.assertEqual(self.new_detail.password,'StAiGhTOrSyoki@#@&')

    def save_detail_test(self):
        """
        test case to test if the detail object is saved into the details list.

        """
        self.new_detail.save_details()
        self.assertEqual(len(Details.details_list),1)

    def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        Details.details_list = []  
    def test_save_many_accounts(self):
        '''
        test to check if we can save multiple details objects to our details list
        '''
        self.new_detail.save_details()
        test_detail = Details("Twitter","georgekilewa","GeO%$#85Hj") 
        test_detail.save_details()
        self.assertEqual(len(Details.details_list),2)
    def test_delete_detail(self):
        """
        test method to test if we can remove an account details from our details_list
        """
        self.new_detail.save_details()
        test_detail= Details("Twitter","georgekilewa","GeO%$#85Hj") 
        test_detail.save_details()

        self.new_detail.delete_details()
        self.assertEqual(len(Details.details_list),1)          
    def test_find_details(self):
        """
        test to check if we can find a detail entry by account name and display the details.
        """
        self.new_detail.save_details()
        test_detail= Details("Twitter","georgekilewa","GeO%$#85Hj") 
        test_detail.save_details()

        the_detail = Details.find_details("Twitter")

        self.assertEqual(the_detail.account,test_detail.account)
    
    def test__detail_exist(self):
        """
        test to check if we can return a true or false based on whether we find or can't find the detail.
        """
        self.new_detail.save_details()
        the__detail = Details("Twitter","georgekilewa","GeO%$#85Hj")  
        the__detail.save_details()
        detail_is_found = Details.if_detail_exist("Twitter")
        self.assertTrue(detail_is_found)

    def test_display_all_saved_details(self):
        '''
        method that displays all the details that has been saved by the user
        '''

        self.assertEqual(Details.display_details(),Details.details_list)
if __name__ == "__main__":
    unittest.main()           