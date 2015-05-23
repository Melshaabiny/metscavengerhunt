from selenium import webdriver
import unittest

def login(browser, url, username, password):
    browser.get(url)

    # enter the username and password.
    username_field = browser.find_element_by_name('user_name')
    username_field.send_keys(username)
    password_field = browser.find_element_by_name('password')
    password_field.send_keys(password)
            # click login button.
    # get the first input button under the first form in login page.
    login_button = browser.find_element_by_xpath("//form[1]/fieldset[1]/input[@type='submit']")
    return login_button

class AcceptanceTest(unittest.TestCase):
    """
    Acceptance tests for Scavenger Hunt Project.

    """

    def setUp(self):
        """
        Setup the test envinronment, such as instantiate webDriver.
        """
        self.browser = webdriver.Firefox()
        self.url = 'http://127.0.0.1:8000/'

    def tearDown(self):
        self.browser.quit()

    # def test_home_menu(self):
    #     self.browser.get(self.url)
    #     # check the title
    #     assert 'Scavenger Hunt' in self.browser.title
    #     body = self.browser.find_element_by_tag_name('body')
    #     # Are menu displayed correctly??
    #     assert 'Home' in body.text
    #     assert 'About' in body.text
    #     assert 'Categories' in body.text
    #     assert 'Create Hunts' in body.text
    #     assert 'Ancient Art' in body.text
    #     assert 'Medieval Art' in body.text
    #     assert 'Asian Art' in body.text
    #     assert 'Modern Art' in body.text
    #     assert 'European Art' in body.text

    # def test_login(self):
    #     """
    #     This test login functionality of the site. 
    #     """
    #     url_extend = 'user_auth/login/'
    #     self.browser.get(self.url + url_extend)

    #     # enter the username and password.
    #     username_field = self.browser.find_element_by_name('user_name')
    #     username_field.send_keys('user4')
    #     password_field = self.browser.find_element_by_name('password')
    #     password_field.send_keys('user')

    #     # click login button.
    #     # get the first input button under the first form in login page.
    #     login_button = self.browser.find_element_by_xpath("//form[1]/fieldset[1]/input[@type='submit']")
    #     try:
    #         login_button.click()
    #     except:
    #         raise Exception("Login Error!")

    # def test_username_not_exist(self):
    #     """
    #     Test if a user input the username that is not exist in the site.
    #     In this case, the login page stays at the same location but shows 
    #     error message that the username does not exist and the user can
    #     click go back button.
    #     """

    #     url_extend = 'user_auth/login/'
    #     # get the first input button under the first form in login page.
    #     username = 'usersomerandomeuser'
    #     password = 'user'
    #     login_button = login(self.browser, self.url + url_extend, username, password)
    #     try:
    #         login_button.click()
    #     except:
    #         raise Exception("Login Error!")

    #     ## check the current url
    #     assert self.browser.current_url == self.url + url_extend

    # def test_profile(self):
    #     """
    #     This test case tests if a logged in user can access to the
    #     profile page properly. Also checks a not logged in user is
    #     blocked from the profile page by checking if the profile
    #     menu is visible to the user.
    #     """

    #     # login in
    #     url_extend = 'user_auth/login/'
    #     username = 'user4'
    #     password = 'user'
    #     login_button = login(self.browser, self.url + url_extend, username, password)
    #     try:
    #         login_button.click()
    #     except:
    #         raise Exception("Login Error!")
    #     # locate the profile memu.
    #     try:
    #         profile_menu = self.browser.find_element_by_id('profile')
    #         profile_menu.click()
    #     except:
    #         raise Exception("Cannot find profile menu!")

    #     # check if we are at the profile page after we clicked the profile menu.
    #     self.assertEqual(self.browser.current_url, self.url + 'user_auth/profile/')

    # def test_forum_access(self):
    #     """
    #     This test case tests if a logged in user can access to the forum.
    #     There are several things to check including if a user is logged in,
    #     the current url...
    #     """

    #     url_extend = 'user_auth/login/'
    #     username = 'user4'
    #     password = 'user'
    #     login_button = login(self.browser, self.url + url_extend, username, password)
    #     try:
    #         login_button.click()
    #     except:
    #         raise Exception("Login Error!")

    #     # go to home.
    #     # self.browser.get(self.url)
    #     # locate the forum button.
    #     try:
    #         forum_button = self.browser.find_element_by_id('forum_link')
    #         # webdriver.ActionChains(self.browser).move_to_element(forum_button).click(forum_button).perform()
    #         forum_button.click()
    #     except:
    #         raise Exception("Forum button cannot be found!")


    #     self.assertEqual(self.browser.current_url, self.url + 'forum/thread/')


########## Hunts test
    def test_go_through_hunt(self):
        """
        This test go through one of the ancient hunt and check error cases.
        """

        url_extend = 'user_auth/login/'
        username = 'user4'
        password = 'user'
        login_button = login(self.browser, self.url + url_extend, username, password)
        try:
            login_button.click()
        except:
            raise Exception("Login Error!")
        # walk through the hunt.
        self.browser.get(self.url + 'hunts/detail/Medieval')

        # go to welcome page, get clue button.
        try:
            self.browser.get(self.url + 'hunts/welcome/2')
            clue_button = self.browser.find_element_by_xpath('//form[1]/input[1]')
            clue_button.click()
        except:
            raise Exception("Cannot find clue button!")

        answers = ["53.37", "27.18.2", "17.190.726"]
        # get the found it button.
        try:
            found_it = self.browser.find_element_by_xpath("//form[2]/input[@type='submit']")
            found_it.click()
        except:
            raise Exception("Cannot find Found it button!")

        # input the answer.
        try:
            answer = self.browser.find_element_by_xpath("//input[@type='text'][@id='input']")
            answer.send_keys(answers[0])
            send = self.browser.find_element_by_xpath("//form[1]/input[@type='submit']")
            send.click()
        except:
            raise Exception("Cannot send the answer!!")

        # click next.
        try:
            next = self.browser.find_element_by_xpath("//form[1]/input[@type='submit']")
            next.click()
        except:
            raise Exception("Cannot find next button!")

        # second answer
        try:
            found_it = self.browser.find_element_by_xpath("//form[2]/input[@type='submit']")
            found_it.click()
        except:
            raise Exception("Cannot find Found it button!")

        # input the answer.
        try:
            answer = self.browser.find_element_by_xpath("//input[@type='text'][@id='input']")
            answer.send_keys(answers[1])
            send = self.browser.find_element_by_xpath("//form[1]/input[@type='submit']")
            send.click()
        except:
            raise Exception("Cannot send the answer!!")

if __name__=="__main__":
    unittest.main()

# def login(browser):
#     browser.get('http://slowlybutconstantly.org/scav_hunt/user_auth/login/')
#     username_field = browser.find_element_by_name('user_name')
#     username_field.send_keys('user4')
#     password_field = browser.find_element_by_name('password')
#     password_field.send_keys('user')
#     return browser


# browser = webdriver.Firefox()
# browser.get('http://slowlybutconstantly.org/scav_hunt') # get the webpage.


# browser.get('http://slowlybutconstantly.org/scav_hunt/user_auth/login/')
# try:
#     username_field = browser.find_element_by_name('user_name')
#     username_field.send_keys('user4')
#     password_field = browser.find_element_by_name('password')
#     password_field.send_keys('user')
# except:
#     raise Exception("Login failed!")

# ############# Ancient Art
# browser.get('http://slowlybutconstantly.org/scav_hunt/hunts/welcome/1')
# assert 'Museum Hunters' in browser.title
# input_clue = browser.find_element_by_tag_name('input')
# input_clue.click()


# ############ Medieval Art
# browser.get('http://slowlybutconstantly.org/scav_hunt/hunts/welcome/2')
# input_clue = browser.find_element_by_tag_name('input')
# input_clue.click()

# ############ Profile page
# # browser = login(browser)
# # profile = browser.find_element_by_id('profile')
# # profile.click()

# browser.quit()

