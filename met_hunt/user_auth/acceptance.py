from selenium import webdriver

def login(browser):
    browser.get('http://slowlybutconstantly.org/scav_hunt/user_auth/login/')
    username_field = browser.find_element_by_name('user_name')
    username_field.send_keys('user4')
    password_field = browser.find_element_by_name('password')
    password_field.send_keys('user')
    return browser


browser = webdriver.Firefox()
browser.get('http://slowlybutconstantly.org/scav_hunt') # get the webpage.

# check the title
assert 'Scavenger Hunt' in browser.title
body = browser.find_element_by_tag_name('body')
# Are menu displayed correctly??
assert 'Home' in body.text
assert 'About' in body.text
assert 'Categories' in body.text
assert 'Create Hunts' in body.text
assert 'Ancient Art' in body.text
assert 'Medieval Art' in body.text
assert 'Asian Art' in body.text
assert 'Modern Art' in body.text
assert 'European Art' in body.text

browser.get('http://slowlybutconstantly.org/scav_hunt/user_auth/login/')
try:
    username_field = browser.find_element_by_name('user_name')
    username_field.send_keys('user4')
    password_field = browser.find_element_by_name('password')
    password_field.send_keys('user')
except:
    raise Exception("Login failed!")

############# Ancient Art
browser.get('http://slowlybutconstantly.org/scav_hunt/hunts/welcome/1')
assert 'Museum Hunters' in browser.title
input_clue = browser.find_element_by_tag_name('input')
input_clue.click()


############ Medieval Art
browser.get('http://slowlybutconstantly.org/scav_hunt/hunts/welcome/2')
input_clue = browser.find_element_by_tag_name('input')
input_clue.click()

############ Profile page
# browser = login(browser)
# profile = browser.find_element_by_id('profile')
# profile.click()

browser.quit()

