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

############# click proceed to create hunt
browser.get('http://slowlybutconstantly.org/scav_hunt/cr_hunt/welcome/')
assert 'Museum Hunters' in browser.title
input_clue = browser.find_element_by_tag_name('input')
input_clue.click()




############At the input title and start place page
body = browser.find_element_by_tag_name('body')
assert 'Enter Title' in body.text
assert 'Enter Starting Point' in body.text

############ Add a title and starting point
title_field = browser.find_element_by_name('title')
title_field.send_keys('My First Title')
start_field = browser.find_element_by_name('start')
start_field.send_keys('Start here')

############ Submit query
submit_title_start = browser.find_element_by_id('submit')
submit_title_start.click()

############ At the add item page
body = browser.find_element_by_tag_name('body')
assert 'Enter Clue:' in body.text
assert 'Add Item:' in body.text

########### Add ten items and clues
add_i = 0
while(add_i < 10):
    clue_field = browser.find_element_by_name('clue')
    clue_field.send_keys('Clue for a hunt')
    item_field = browser.find_element_by_id('id_item')
    for option in item_field.find_element_by_tag_name('option'):
        if option.text == '03.12.14':
            option.click()
    submit_itcl = browser.find_element_by_id('submit')
    submit_itcl.click()
    add_i = add_i + 1


browser.quit()

