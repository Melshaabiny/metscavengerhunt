

from selenium import webdriver

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
    
browser.quit()

